n = int(input())
answer = []

for num in range(1, n+1):
    strNum = str(num)
    temp = ""

    for i in range(len(strNum)):
        if strNum[i] == '3' or strNum[i] == '6' or strNum[i] == '9':
            temp += '-'

    if len(temp) == 0:  # 369 없으면
        answer.append(num)
    else:
        answer.append(temp)

print(' '.join(map(str,answer)))