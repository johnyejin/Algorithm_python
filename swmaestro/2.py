# 코딩지는 무조건 2 * 2
def dfs(i, j):
    global n, m, arr

    for a in range(1, 3):
        for b in range(1, 3):
            if i + a >= n or j + b >= m:
                continue
            if arr[i+a][j+b] == 0:
                return False

    return True


t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    flag = True

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                continue
            flag = dfs(i, j)
            if flag is False:
                break
        if flag is False:
            break

    if flag is False:
        print('NO')
    else:
        print('YES')