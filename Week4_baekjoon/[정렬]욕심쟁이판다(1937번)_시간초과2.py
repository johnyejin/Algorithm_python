n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
day = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if day[x][y]:
        return day[x][y]
    day[x][y] = 1

    for a in range(4):
        nx, ny = x + dx[a], y + dy[a]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
            day[x][y] = max(day[x][y], dfs(nx, ny) + 1)

    return day[x][y]


for i in range(n):
    for j in range(n):
        day[i][j] = dfs(i, j)

print(max(map(max, day)))  # 2차원 배열에서 최대값 찾기