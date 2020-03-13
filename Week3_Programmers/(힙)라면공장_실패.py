def solution(stock, dates, supplies, k):
    answer = 0  # 최소 몇 번 공급받아야 하는지
    last_supply = 0  # 마지막으로 공급받은 날짜

    idx = 0
    for date in range(k):
        stock -= 1

        if dates[idx] == date:
            if idx + 1 == len(dates) and stock < k - dates[idx]:
                answer += 1
                break

            # 다음 공급까지 필요없으면 continue, 아니면 공급 받기
            if stock == 0 or stock < dates[idx+1] - dates[idx]:
                stock += supplies[idx]
                answer += 1
                last_supply = dates[idx]

            idx += 1

        # print(date, stock, idx, answer, last_supply)

    return answer