Deadlock Detection (using DFS)

Files included:
- main.py   -> the python code
- sample_no_deadlock.txt
- sample_multiple_deadlocks.txt
- README.txt

How to run:
open terminal (or powershell), go to the folder, then run:
    python main.py
    type sample_no_deadlock.txt
or
    python main.py
    type sample_multiple_deadlocks.txt

Input format:
- each line has 2 names (u v) meaning edge u -> v
- lines starting with # are ignored
- nodes can be processes/resources like P1 R1 etc.

Output:
- if there is no deadlock, it prints "No deadlocks found."
- if there are cycles, it prints how many and lists them
  example:
    Total deadlock cycles: 3
    Cycle 1 : P1 -> R1 -> P2 -> R2 -> P1
    Cycle 2 : P3 -> R3 -> P4 -> R4 -> P3
    Cycle 3 : P1 -> R1 -> P2 -> R3 -> P1

Design notes:
- used DFS recursion
- to avoid repeating the same cycle, I only allow exploring nodes >= the start node
- this way each cycle is printed once
- simple adjacency list (dict with lists) is used
- only python standard library

Assumptions:
- graph is directed
- input file is clean (no weird characters)
- cycles represent deadlocks
