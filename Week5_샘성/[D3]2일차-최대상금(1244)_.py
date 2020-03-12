# 캐어려움
def dfs(current, cnt):
    global change, cardList, answer
    if cnt == change:
        answer = max(int(''.join(map(str, cardList))), answer)
        return

    for i in range(current, len(cardList)):
        for j in range(i+1, len(cardList)):
            if cardList[i] <= cardList[j]:
                cardList[i], cardList[j] = cardList[j], cardList[i]
                dfs(i, cnt + 1)
                cardList[i], cardList[j] = cardList[j], cardList[i]


t = int(input())
for case in range(1, t+1):
    card, change = input().split()
    change = int(change)
    cardList = list(map(int, card))
    answer = 0

    dfs(0, 0)

    print("#%d" % case, answer)
