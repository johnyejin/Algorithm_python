string = list(input())

# dial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# dic = {'A':2, 'B':2, 'C':2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4, 'I':4}
# dic = {'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}

for i in range(len(string)):
    if string[i] == 'A' or string[i] == 'B' or string[i] == 'C':
        string[i] = 2
    elif string[i] == 'D' or string[i] == 'E' or string[i] == 'F':
        string[i] = 3
    elif string[i] == 'G' or string[i] == 'H' or string[i] == 'I':
        string[i] = 4
    elif string[i] == 'J' or string[i] == 'K' or string[i] == 'L':
        string[i] = 5
    elif string[i] == 'M' or string[i] == 'N' or string[i] == 'O':
        string[i] = 6
    elif string[i] == 'P' or string[i] == 'Q' or string[i] == 'R' or string[i] == 'S':
        string[i] = 7
    elif string[i] == 'T' or string[i] == 'U' or string[i] == 'V':
        string[i] = 8
    else:
        string[i] = 9

print(sum(string) + len(string))