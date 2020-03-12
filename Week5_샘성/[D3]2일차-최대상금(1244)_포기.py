t = int(input())
for case in range(1, t+1):
    card, change = input().split()
    change = int(change)
    cardList = list(map(int, card))

    for c in range(1, change+1):
        flag = False  # 더이상 바꿀게 없는데 횟수가 남았다?=false, 아니면 true
        for i in range(len(cardList)):
            if cardList[i] == max(cardList[i:]):
                continue

            maxCard = cardList[i]
            maxIdx = 0
            for j in range(len(cardList)-1, i, -1):
                if maxCard < cardList[j]:
                    maxCard = cardList[j]
                    maxIdx = j

            cardList[i], cardList[maxIdx] = cardList[maxIdx], cardList[i]
            flag = True
            break

        # 더이상 바꿀게 없는데 횟수가 남았을때 예외처리
        if flag is False:
            if (change + 1 - c) % 2 == 1:
                if cardList[len(cardList)-2] == max(cardList):
                    break
                cardList[len(cardList)-2], cardList[len(cardList)-1] = cardList[len(cardList)-1], cardList[len(cardList)-2]
            break
        # print(cardList)
    print("#%d" % case, ''.join(map(str, cardList)))
