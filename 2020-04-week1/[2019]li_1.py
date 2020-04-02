def divide(num):
    arr = []
    ans = 10000

    for i in range(1, num // 2):
        if num % i == 0:
            # if i == num // i:
            #     arr.append(i)
            #     break
            arr.append(i)
            arr.append(num // i)

            # 최소 확인
            if abs(num // i - i) < ans:
                ans = abs(num // i - i)
            print(ans)

    return arr, ans

def solution(n):
    answer = 0  # 최솟값

    # 소인수분해
    arr, answer = divide(n)
    arr.sort()

    return answer


print(solution(8))