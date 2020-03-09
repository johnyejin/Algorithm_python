string = input().upper()
dic = dict()

for i in range(len(string)):
    if string[i] in dic:
        dic[string[i]] += 1
    else:
        dic[string[i]] = 1

maxCnt = max(dic.values())
answer = []
for key, value in dic.items():
    if value == maxCnt:
        answer.append(key)

if len(answer) != 1:
    print('?')
else:
    print(answer[0])