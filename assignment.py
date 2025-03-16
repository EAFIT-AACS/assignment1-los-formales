def find_equivalence_states(Q, F, function, alphabet):   # Function to find the equivalence states
    pairs = [[0 for j in range(i + 1, len(Q))] for i in range(len(Q)-1)]  # Stores the pairs of states in a triangular matrix
    equiv = []          # Create a list to store the equivalent states
    for i in range(len(Q)-1):
        for j in range(len(pairs[i])):          # Iterate over the pairs of states
            if (i in F and j+i+1 not in F) or (i not in F and j+i+1 in F):
                # If one of the states is final and the other is not, mark the pair as 1
                pairs[i][j] = 1

    mark = True        # Variable to control the while loop
    while mark:         # Iterate over the pairs of states until no more new pairs are marked
        mark = False
        for i in range(len(Q)-1):
            for j in range(len(pairs[i])):
                if pairs[i][j] == 0:
                    # If the pair is not marked, iterate over the alphabet to check the transitions
                    for l in alphabet:
                        q1 = function[i][alphabet.index(l)]
                        q2 = function[j+i+1][alphabet.index(l)]
                        if q1 > q2:             # Swap the states if q1 > q2 to make q1 < q2
                            q1, q2 = q2, q1
                        if (q1 != q2) and pairs[q1][q2-q1-1] == 1:
                            # If the resulting pair is marked and the states are different, mark the pair as 1
                            pairs[i][j] = 1
                            mark = True     # Update the variable to continue the loop
                            break           # Break the loop if the pair is marked
    for i in range(len(Q)-1):       # Iterate over the pairs of states
        for j in range(len(pairs[i])):
            if pairs[i][j] == 0:        # If the pair is not marked, store the pair in the list
                equiv.append((i, j+i+1))

    print(' '.join(map(str, equiv)))        # Print the equivalent states


current_line = 1      # Variable of control to read the lines of the file

with open('DFAs.txt', 'r') as archivo:      # Open the file
    lines = [line.strip() for line in archivo.readlines()]      # Read the file and store the lines in a list

for _ in range(int(lines[0])):              # Iterate over the number of cases
    # Read the number of states, the alphabet and the final states
    Q_number = int(lines[current_line])
    alphabet = lines[current_line + 1].split()
    F = list(map(int, lines[current_line + 2].split()))
    function = [[] for _ in range(Q_number)]    # Create a matrix to store the transitions
    for j in range(Q_number):
        function[j] = list(map(int, lines[current_line + 3 + j].split()[1:]))   # Store the transitions
    find_equivalence_states(range(Q_number), F, function, alphabet)     # Call the function to find the equivalence states
    current_line += 3 + Q_number      # Update the start line for the next case   



