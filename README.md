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

In the DFA file, there are six cases. The first two are from the book, the next two are from the example input in the activity, and the last two were created by us.

### Case 1:
Lecture 14, example 14.1

![image](https://github.com/user-attachments/assets/773fd565-4e45-411f-a504-ed5657ffb68d)

**Expected output**

![image](https://github.com/user-attachments/assets/a3982071-3f47-4dd7-8e95-1210eebc98c3)

**Output:**
```
(1, 2) (3, 4)
```
### Case 2:
Lecture 13, example 13.4
![image](https://github.com/user-attachments/assets/a7329712-5b93-4886-96ea-818113736d04)

**Expected output**

![image](https://github.com/user-attachments/assets/0709d680-9cd2-41e0-a816-c2f4c8f2a6ad)

**Output:**

```
(1, 2) (3, 4) (3, 5) (4, 5)
```

### Case 3:

**Input 3**

![image](https://github.com/user-attachments/assets/6daf7f7e-445b-4154-b38d-bc895fc6d0b7)

**Expected output**

```
(0, 3) (1, 4) (2, 5)
```

**Output:**

```
(0, 3) (1, 4) (2, 5)
```


### Case 4:

**Input 4**

![image](https://github.com/user-attachments/assets/e73b6415-4036-43fd-8ee6-75464e4572d7)

**Expected output**

```
(0, 1)
```

**Output:**

```
(0, 1)
```

### Case 5:

**Input**

```
3
0 1
0 2
0 1 0
1 2 0
2 1 2
```

**Output:**

```
(0, 2)
```


### Case 6:

**Input**

```
4
0 1
0
0 1 2
1 0 3
2 0 3
3 0 3
```

**Output:**

```
(1, 2) (1, 3) (2, 3)
```


## Explanation of the algorithm
The algorithm finds equivalent states in a Deterministic Finite Automaton (DFA) using a triangular matrix to store pairs of states. Initially, pairs where one state is final and the other is not are marked as non-equivalent. The algorithm then iterates through the remaining pairs, checking their transitions for each symbol in the alphabet. If the transitions lead to previously marked non-equivalent states, the current pair is also marked as non-equivalent. This process continues until no new pairs are marked. Finally, pairs that remain unmarked are considered equivalent and are printed.
