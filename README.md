# ASSIGNMENT 1

## Authors
- **Laura Restrepo**
- **Johan Samuel Rico**

## Class Number
7308

## Versions
- **Operating System**: Windows 10
- **Programming Language**: Python 3.12
- **Tools Used**: PyCharm

## Instructions for Running the Implementation

1. Place DFAs.txt in the same folder as the script.
2. Run the script to read DFAs.txt.

In the DFAs file, there are four cases. The first two are from the book, and the last two were created by us

### Case 1:
![image](https://github.com/user-attachments/assets/773fd565-4e45-411f-a504-ed5657ffb68d)
![image](https://github.com/user-attachments/assets/a3982071-3f47-4dd7-8e95-1210eebc98c3)
Lecture 14, example 14.1

### Case 2:
![image](https://github.com/user-attachments/assets/a7329712-5b93-4886-96ea-818113736d04)
![image](https://github.com/user-attachments/assets/0709d680-9cd2-41e0-a816-c2f4c8f2a6ad)
Lecture 13, example 13.4

### Case 3:


### Case 4:


## Explanation of the algorithm
The algorithm finds equivalent states in a Deterministic Finite Automaton (DFA) using a triangular matrix to store pairs of states. Initially, pairs where one state is final and the other is not are marked as non-equivalent. The algorithm then iterates through the remaining pairs, checking their transitions for each symbol in the alphabet. If the transitions lead to previously marked non-equivalent states, the current pair is also marked as non-equivalent. This process continues until no new pairs are marked. Finally, pairs that remain unmarked are considered equivalent and are printed.
