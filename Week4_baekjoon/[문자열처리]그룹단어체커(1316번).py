n = int(input())
answer = 0

for case in range(n):
    string = input()
    arr = []
    flag = False

    for i in range(len(string)):
        if string[i] in arr:
            if string[i-1] != string[i]:
                flag = True
                break
        else:
            arr.append(string[i])

    if not flag:
        answer += 1

print(answer)