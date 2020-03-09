dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
string = input()
answer = 0

for i in range(len(string)):
    for d in dial:
        if string[i] in d:
            answer += dial.index(d) + 3

print(answer)