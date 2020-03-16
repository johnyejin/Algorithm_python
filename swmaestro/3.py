def division(n, k):
    global div
    if div[n][k] != -1:
        return div[n][k]
    if k > n:
        return 0
    a = division(n-1, k-1)
    div[n-1][k-1] = a
    b = division(n-k, k)
    div[n-k][k] = b
    return a + b


n, k = map(int, input().split())  # 원본 배열의 원소 수, 나눌 부분 배열의 수
original = list(map(int, input().split()))
print(original)
div = [[0] * n for _ in range(n)]
print(div)

# 리스트 분할
for i in range(6):
    for j in range(1, 6):
        if j==1:
            div[i][1] = 1
        else:
            div[i][j] = -1

print(div)
print(division(n, k))
print(div)
# 분할한 리스트들 패널티 계산