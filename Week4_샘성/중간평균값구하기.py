t = int(input())

for case in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop(0)
    arr.pop(-1)

    answer = sum(arr) // len(arr)
    if sum(arr) / len(arr) - float(answer) >= 0.5:
        answer += 1
    print("#%d" % (case + 1), answer)