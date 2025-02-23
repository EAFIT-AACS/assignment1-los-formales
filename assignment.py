def find_equivalence_states(Q, F, function, alphabet):
    pairs = [[0 for j in range(i + 1, len(Q))] for i in range(len(Q)-1)]
    equiv = []
    for i in range(len(Q)-1):
        for j in range(len(pairs[i])):
            if (i in F and j+i+1 not in F) or (i not in F and j+i+1 in F):
                pairs[i][j] = 1
    mark = True
    while mark:
        mark = False
        for i in range(len(Q)-1):
            for j in range(len(pairs[i])):
                if pairs[i][j] == 0:
                    for l in alphabet:
                        q1 = function[i][alphabet.index(l)]
                        q2 = function[j+i+1][alphabet.index(l)]
                        if q1 > q2:
                            q1, q2 = q2, q1
                        if (q1 != q2) and pairs[q1][q2-q1-1] == 1:
                            pairs[i][j] = 1
                            mark = True
                            break
        if not mark:
            for i in range(len(Q)-1):
                for j in range(len(pairs[i])):
                    if pairs[i][j] == 0:
                        equiv.append((i, j+i+1))

    print(' '.join(map(str, equiv)))


start_line = 1

with open('DFAs.txt', 'r') as archivo:
    lines = [line.strip() for line in archivo.readlines()]

for _ in range(int(lines[0])):
    Q_number = int(lines[start_line])
    alphabet = lines[start_line + 1].split()
    F = list(map(int, lines[start_line + 2].split()))
    function = [[] for _ in range(Q_number)]
    for j in range(Q_number):
        function[j] = list(map(int, lines[start_line + 3 + j].split()[1:]))
    find_equivalence_states(range(Q_number), F, function, alphabet)
    start_line += 3 + Q_number