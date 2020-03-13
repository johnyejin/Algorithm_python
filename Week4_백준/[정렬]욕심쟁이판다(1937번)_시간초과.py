n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maxCnt = 0
cnt = 1

def dfs(x, y):
    global cnt
    # 다음 방문지가 현재보다 크면 방문
    visit[x][y] = 1

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        # 현재 위치가 시작지점이면 cnt = 1로 초기화. 이거 안해주면 상하좌우 모든 방향 탐색하면서 cnt++함
        if x == i and y == j:
            cnt = 1
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] != 1 and arr[nx][ny] > arr[x][y]:
            cnt += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        visit = [[0] * n for _ in range(n)]  # 탐색할때마다 초기화
        cnt = 1
        dfs(i, j)
        if cnt > maxCnt:
            maxCnt = cnt

print(maxCnt)