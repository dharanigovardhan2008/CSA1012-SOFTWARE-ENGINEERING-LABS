from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": True},
    {"id": 2, "title": "Build Flask Application", "completed": False},
    {"id": 3, "title": "Push Image to Docker Hub", "completed": False},
]

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>EX21 — TaskFlow</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        :root {
            --bg: #f5f7fb;
            --surface: rgba(255,255,255,.78);
            --surface-solid: #ffffff;
            --text: #111827;
            --muted: #6b7280;
            --border: rgba(17,24,39,.08);
            --primary: #111827;
            --primary-hover: #2d3748;
            --accent: #6366f1;
            --success: #16a34a;
            --danger: #dc2626;
            --shadow: 0 30px 80px rgba(15,23,42,.10);
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            min-height: 100vh;
            font-family:
                Inter,
                ui-sans-serif,
                system-ui,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;

            background:
                radial-gradient(
                    circle at 15% 15%,
                    rgba(99,102,241,.12),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 85% 85%,
                    rgba(14,165,233,.10),
                    transparent 30%
                ),
                var(--bg);

            color: var(--text);
            overflow-x: hidden;
        }

        /* Ambient background */

        .orb {
            position: fixed;
            width: 320px;
            height: 320px;
            border-radius: 50%;
            filter: blur(90px);
            opacity: .25;
            pointer-events: none;
            z-index: -1;
            animation: float 12s ease-in-out infinite;
        }

        .orb.one {
            background: #818cf8;
            top: -120px;
            left: -100px;
        }

        .orb.two {
            background: #38bdf8;
            bottom: -140px;
            right: -100px;
            animation-delay: -5s;
        }

        @keyframes float {
            0%, 100% {
                transform: translate3d(0,0,0) scale(1);
            }

            50% {
                transform: translate3d(30px,-25px,0) scale(1.08);
            }
        }

        .shell {
            width: min(1180px, calc(100% - 40px));
            margin: 0 auto;
            padding: 48px 0 70px;
        }

        /* Header */

        .topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 34px;

            animation: fadeDown .7s ease both;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 13px;
        }

        .brand-mark {
            width: 42px;
            height: 42px;
            border-radius: 13px;

            background: #111827;

            display: grid;
            place-items: center;

            box-shadow:
                0 10px 25px rgba(17,24,39,.18);

            position: relative;
            overflow: hidden;
        }

        .brand-mark::before {
            content: "";
            width: 15px;
            height: 15px;
            border: 2px solid white;
            border-radius: 5px;
        }

        .brand-title {
            font-size: 17px;
            font-weight: 750;
            letter-spacing: -.02em;
        }

        .brand-subtitle {
            color: var(--muted);
            font-size: 12px;
            margin-top: 2px;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;

            padding: 9px 13px;
            border: 1px solid var(--border);
            border-radius: 999px;

            background: rgba(255,255,255,.62);
            backdrop-filter: blur(16px);

            font-size: 12px;
            color: var(--muted);
        }

        .status-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #22c55e;

            box-shadow: 0 0 0 5px rgba(34,197,94,.10);

            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% {
                box-shadow: 0 0 0 4px rgba(34,197,94,.10);
            }

            50% {
                box-shadow: 0 0 0 8px rgba(34,197,94,.02);
            }
        }

        /* Hero */

        .hero {
            display: grid;
            grid-template-columns: 1.4fr .6fr;
            gap: 24px;
            margin-bottom: 24px;
        }

        .hero-card {
            position: relative;
            overflow: hidden;

            border-radius: 28px;
            padding: 38px;

            background:
                linear-gradient(
                    135deg,
                    rgba(255,255,255,.92),
                    rgba(255,255,255,.62)
                );

            border: 1px solid rgba(255,255,255,.8);

            box-shadow: var(--shadow);
            backdrop-filter: blur(24px);

            animation: fadeUp .7s .05s ease both;
        }

        .hero-card::after {
            content: "";
            position: absolute;
            width: 280px;
            height: 280px;
            right: -130px;
            top: -140px;
            border-radius: 50%;

            background: rgba(99,102,241,.09);
            filter: blur(10px);
        }

        .eyebrow {
            display: inline-flex;
            padding: 7px 11px;
            border-radius: 999px;

            background: rgba(99,102,241,.08);
            color: #4f46e5;

            font-size: 11px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;

            margin-bottom: 17px;
        }

        h1 {
            font-size: clamp(38px, 6vw, 64px);
            line-height: .98;
            letter-spacing: -.055em;
            max-width: 680px;
        }

        .hero-description {
            color: var(--muted);
            margin-top: 18px;
            max-width: 620px;
            line-height: 1.7;
            font-size: 15px;
        }

        .tech-line {
            display: flex;
            gap: 9px;
            flex-wrap: wrap;
            margin-top: 25px;
        }

        .tech {
            border: 1px solid var(--border);
            background: rgba(255,255,255,.72);
            padding: 8px 11px;
            border-radius: 10px;
            font-size: 11px;
            color: #4b5563;
        }

        /* Progress card */

        .progress-card {
            border-radius: 28px;
            padding: 30px;

            background: #111827;
            color: white;

            box-shadow:
                0 30px 70px rgba(17,24,39,.20);

            animation: fadeUp .7s .15s ease both;

            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .progress-label {
            font-size: 12px;
            color: rgba(255,255,255,.55);
            text-transform: uppercase;
            letter-spacing: .09em;
        }

        .progress-number {
            font-size: 58px;
            font-weight: 750;
            letter-spacing: -.06em;
            margin-top: 10px;
        }

        .progress-track {
            height: 7px;
            background: rgba(255,255,255,.12);
            border-radius: 99px;
            overflow: hidden;
            margin-top: 20px;
        }

        .progress-fill {
            height: 100%;
            width: {{ progress }}%;
            border-radius: inherit;

            background: linear-gradient(
                90deg,
                #818cf8,
                #38bdf8
            );

            animation: progressGrow 1.2s .5s ease both;
            transform-origin: left;
        }

        @keyframes progressGrow {
            from {
                transform: scaleX(0);
            }
            to {
                transform: scaleX(1);
            }
        }

        .progress-meta {
            display: flex;
            justify-content: space-between;
            color: rgba(255,255,255,.55);
            font-size: 12px;
            margin-top: 10px;
        }

        /* Main workspace */

        .workspace {
            display: grid;
            grid-template-columns: 1fr 310px;
            gap: 24px;
        }

        .panel {
            border-radius: 25px;
            background: var(--surface);
            border: 1px solid rgba(255,255,255,.85);
            box-shadow: var(--shadow);
            backdrop-filter: blur(24px);

            animation: fadeUp .7s .25s ease both;
        }

        .tasks-panel {
            padding: 25px;
        }

        .panel-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .panel-title {
            font-size: 19px;
            font-weight: 750;
            letter-spacing: -.025em;
        }

        .count {
            padding: 6px 9px;
            border-radius: 8px;
            background: #f1f3f7;
            color: #6b7280;
            font-size: 11px;
            font-weight: 700;
        }

        /* Add task */

        .add-form {
            display: flex;
            gap: 10px;
            margin-bottom: 22px;
        }

        .input-wrap {
            flex: 1;
            position: relative;
        }

        .input-wrap input {
            width: 100%;
            height: 52px;

            border: 1px solid var(--border);
            border-radius: 14px;

            background: rgba(255,255,255,.85);

            padding: 0 16px;
            outline: none;

            font-size: 14px;
            color: var(--text);

            transition:
                border .2s ease,
                box-shadow .2s ease,
                transform .2s ease;
        }

        .input-wrap input:focus {
            border-color: rgba(99,102,241,.35);

            box-shadow:
                0 0 0 4px rgba(99,102,241,.08);

            transform: translateY(-1px);
        }

        .add-button {
            height: 52px;
            border: none;
            border-radius: 14px;

            background: #111827;
            color: white;

            padding: 0 20px;

            font-weight: 700;
            cursor: pointer;

            transition:
                transform .2s ease,
                background .2s ease,
                box-shadow .2s ease;
        }

        .add-button:hover {
            background: #2d3748;
            transform: translateY(-2px);

            box-shadow:
                0 12px 25px rgba(17,24,39,.16);
        }

        .add-button:active {
            transform: translateY(0) scale(.98);
        }

        /* Tasks */

        .task-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .task {
            display: flex;
            align-items: center;
            gap: 14px;

            padding: 15px;

            border: 1px solid transparent;
            border-radius: 16px;

            background: rgba(255,255,255,.68);

            transition:
                transform .25s ease,
                border-color .25s ease,
                box-shadow .25s ease,
                background .25s ease;

            animation: taskIn .45s ease both;
        }

        .task:hover {
            transform: translateY(-3px) translateX(2px);

            border-color: rgba(99,102,241,.12);

            background: white;

            box-shadow:
                0 14px 30px rgba(15,23,42,.07);
        }

        @keyframes taskIn {
            from {
                opacity: 0;
                transform: translateY(12px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .check {
            width: 20px;
            height: 20px;
            border-radius: 7px;

            border: 1.5px solid #cbd5e1;
            background: white;

            display: grid;
            place-items: center;

            cursor: pointer;
            flex-shrink: 0;

            transition: .2s ease;
        }

        .check:hover {
            border-color: #6366f1;
            transform: scale(1.08);
        }

        .check.checked {
            background: #111827;
            border-color: #111827;
        }

        .check.checked::after {
            content: "";
            width: 7px;
            height: 4px;
            border-left: 2px solid white;
            border-bottom: 2px solid white;
            transform: rotate(-45deg) translate(1px,-1px);
        }

        .task-content {
            flex: 1;
            min-width: 0;
        }

        .task-title {
            font-size: 14px;
            font-weight: 650;

            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;

            transition: .2s ease;
        }

        .task.completed .task-title {
            color: #9ca3af;
            text-decoration: line-through;
        }

        .delete {
            width: 32px;
            height: 32px;

            border: none;
            border-radius: 9px;

            background: transparent;
            color: #9ca3af;

            cursor: pointer;

            transition: .2s ease;
        }

        .delete:hover {
            background: rgba(220,38,38,.08);
            color: var(--danger);
            transform: scale(1.05);
        }

        /* Side statistics */

        .side {
            display: flex;
            flex-direction: column;
            gap: 14px;

            animation: fadeUp .7s .35s ease both;
        }

        .stat {
            padding: 22px;
            border-radius: 21px;

            background: var(--surface);
            border: 1px solid rgba(255,255,255,.8);

            box-shadow: 0 18px 45px rgba(15,23,42,.07);

            transition:
                transform .25s ease,
                box-shadow .25s ease;
        }

        .stat:hover {
            transform: translateY(-4px);
            box-shadow: 0 24px 50px rgba(15,23,42,.11);
        }

        .stat-label {
            font-size: 11px;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: .08em;
        }

        .stat-value {
            margin-top: 7px;
            font-size: 32px;
            font-weight: 750;
            letter-spacing: -.04em;
        }

        .stat-description {
            margin-top: 5px;
            font-size: 12px;
            color: var(--muted);
        }

        .docker-card {
            padding: 23px;
            border-radius: 21px;

            background:
                linear-gradient(
                    135deg,
                    #111827,
                    #1f2937
                );

            color: white;

            box-shadow:
                0 20px 50px rgba(17,24,39,.18);
        }

        .docker-title {
            font-size: 14px;
            font-weight: 700;
        }

        .docker-text {
            margin-top: 8px;
            color: rgba(255,255,255,.55);
            font-size: 12px;
            line-height: 1.6;
        }

        .docker-line {
            height: 1px;
            background: rgba(255,255,255,.1);
            margin: 17px 0;
        }

        .container-status {
            display: flex;
            align-items: center;
            gap: 8px;

            font-size: 12px;
            color: rgba(255,255,255,.8);
        }

        .container-status::before {
            content: "";
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #22c55e;
            box-shadow: 0 0 12px rgba(34,197,94,.65);
        }

        /* Footer */

        footer {
            text-align: center;
            margin-top: 30px;

            color: #9ca3af;
            font-size: 11px;

            animation: fadeUp .7s .45s ease both;
        }

        @keyframes fadeUp {
            from {
                opacity: 0;
                transform: translateY(22px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeDown {
            from {
                opacity: 0;
                transform: translateY(-12px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Responsive */

        @media (max-width: 900px) {
            .hero {
                grid-template-columns: 1fr;
            }

            .workspace {
                grid-template-columns: 1fr;
            }

            .side {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
            }

            .docker-card {
                grid-column: 1 / -1;
            }
        }

        @media (max-width: 650px) {
            .shell {
                width: min(100% - 24px, 1180px);
                padding-top: 24px;
            }

            .topbar {
                margin-bottom: 20px;
            }

            .status {
                display: none;
            }

            .hero-card,
            .progress-card {
                padding: 25px;
                border-radius: 22px;
            }

            h1 {
                font-size: 42px;
            }

            .tasks-panel {
                padding: 18px;
            }

            .add-form {
                flex-direction: column;
            }

            .add-button {
                width: 100%;
            }

            .side {
                grid-template-columns: 1fr 1fr;
            }

            .docker-card {
                grid-column: 1 / -1;
            }
        }

        @media (max-width: 430px) {
            .side {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

<div class="orb one"></div>
<div class="orb two"></div>

<div class="shell">

    <header class="topbar">

        <div class="brand">

            <div class="brand-mark"></div>

            <div>
                <div class="brand-title">TaskFlow</div>
                <div class="brand-subtitle">
                    EX21 · Flask + Docker
                </div>
            </div>

        </div>

        <div class="status">
            <span class="status-dot"></span>
            Application healthy
        </div>

    </header>


    <section class="hero">

        <div class="hero-card">

            <span class="eyebrow">
                Productivity workspace
            </span>

            <h1>
                Focus on what<br>
                matters.
            </h1>

            <p class="hero-description">
                A minimal, fast and elegant task management
                experience built with Flask and containerized
                using Docker.
            </p>

            <div class="tech-line">
                <span class="tech">Python</span>
                <span class="tech">Flask</span>
                <span class="tech">Docker</span>
                <span class="tech">Gunicorn</span>
            </div>

        </div>


        <div class="progress-card">

            <div>
                <div class="progress-label">
                    Completion
                </div>

                <div class="progress-number">
                    {{ progress }}%
                </div>
            </div>

            <div>
                <div class="progress-track">
                    <div class="progress-fill"></div>
                </div>

                <div class="progress-meta">
                    <span>{{ completed }} completed</span>
                    <span>{{ pending }} remaining</span>
                </div>
            </div>

        </div>

    </section>


    <section class="workspace">

        <div class="panel tasks-panel">

            <div class="panel-header">

                <div class="panel-title">
                    Your tasks
                </div>

                <div class="count">
                    {{ tasks|length }} total
                </div>

            </div>


            <form class="add-form" method="POST" action="/add">

                <div class="input-wrap">

                    <input
                        type="text"
                        name="title"
                        placeholder="What needs to be done?"
                        autocomplete="off"
                        required
                    >

                </div>

                <button class="add-button" type="submit">
                    Add task
                </button>

            </form>


            <div class="task-list">

                {% for task in tasks %}

                <div class="task {% if task.completed %}completed{% endif %}">

                    <a
                        href="/toggle/{{ task.id }}"
                        style="text-decoration:none;"
                    >

                        <div class="check {% if task.completed %}checked{% endif %}">
                        </div>

                    </a>


                    <div class="task-content">

                        <div class="task-title">
                            {{ task.title }}
                        </div>

                    </div>


                    <a
                        href="/delete/{{ task.id }}"
                        style="text-decoration:none;"
                    >

                        <button
                            class="delete"
                            type="button"
                            aria-label="Delete task"
                        >
                            ×
                        </button>

                    </a>

                </div>

                {% endfor %}

            </div>

        </div>


        <aside class="side">

            <div class="stat">

                <div class="stat-label">
                    Total
                </div>

                <div class="stat-value">
                    {{ tasks|length }}
                </div>

                <div class="stat-description">
                    Tasks in your workspace
                </div>

            </div>


            <div class="stat">

                <div class="stat-label">
                    Completed
                </div>

                <div class="stat-value">
                    {{ completed }}
                </div>

                <div class="stat-description">
                    Successfully finished
                </div>

            </div>


            <div class="stat">

                <div class="stat-label">
                    Pending
                </div>

                <div class="stat-value">
                    {{ pending }}
                </div>

                <div class="stat-description">
                    Still in progress
                </div>

            </div>


            <div class="docker-card">

                <div class="docker-title">
                    Container status
                </div>

                <div class="docker-text">
                    This application is running inside
                    a Docker container using Gunicorn.
                </div>

                <div class="docker-line"></div>

                <div class="container-status">
                    Running · Port 5000
                </div>

            </div>

        </aside>

    </section>


    <footer>
        EX21 · Flask To-Do Application · Docker Containerization
    </footer>

</div>

</body>
</html>
"""


@app.route("/")
def home():

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    pending = len(tasks) - completed

    progress = round(
        (completed / len(tasks)) * 100
    ) if tasks else 0

    return render_template_string(
        HTML,
        tasks=tasks,
        completed=completed,
        pending=pending,
        progress=progress
    )


@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title", "").strip()

    if title:

        new_id = max(
            [task["id"] for task in tasks],
            default=0
        ) + 1

        tasks.append({
            "id": new_id,
            "title": title,
            "completed": False
        })

    return redirect("/")


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):

    for task in tasks:

        if task["id"] == task_id:
            task["completed"] = not task["completed"]

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    global tasks

    tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    return redirect("/")


@app.route("/health")
def health():

    return {
        "status": "healthy",
        "application": "EX21 Flask To-Do",
        "containerized": True
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )