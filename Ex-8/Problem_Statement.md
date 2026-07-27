# Experiment 08 – Find Cyclomatic Complexity using Raptor

## Aim

To calculate the Cyclomatic Complexity of a software program using the given Control Flow Graph (CFG) parameters and represent the calculation using the Raptor tool.

---

## Problem Statement

Cyclomatic Complexity is a software testing metric used to measure the complexity of a software program. It indicates the number of linearly independent execution paths through the source code. Cyclomatic Complexity helps software developers and testers determine the effort required for testing and maintaining a program.

Cyclomatic Complexity can be calculated using either of the following formulas:

- **V(G) = E − N + 2**
- **V(G) = E − N + P**

where:

- **E** = Number of edges in the control flow graph
- **N** = Number of nodes in the control flow graph
- **P** = Number of predicate (decision) nodes

Given:

- Number of Edges (E) = **17**
- Number of Nodes (N) = **13**
- Number of Predicate Nodes (P) = **5**

Using the **Raptor** tool, design a flowchart to calculate the Cyclomatic Complexity using the given values and display the result.

---

## Objectives

- Understand the concept of Cyclomatic Complexity.
- Learn how to calculate complexity using a Control Flow Graph.
- Design a flowchart using Raptor.
- Display the calculated Cyclomatic Complexity.

---

## Requirements

The flowchart should perform the following operations:

1. Start the program.
2. Initialize the values:
   - E = 17
   - N = 13
   - P = 5
3. Calculate Cyclomatic Complexity using:
   - V(G) = E − N + P
4. Display the calculated Cyclomatic Complexity.
5. Stop the program.

---

## Formula Used

Cyclomatic Complexity:

```
V(G) = E − N + P
```

Calculation:

```
V(G) = 17 − 13 + 5
     = 9
```

**Cyclomatic Complexity = 9**

---

## Tools Required

- Raptor

---

## Expected Outcome

A Raptor flowchart that calculates and displays the Cyclomatic Complexity of the given Control Flow Graph. The calculated Cyclomatic Complexity for the given graph is **9**.
