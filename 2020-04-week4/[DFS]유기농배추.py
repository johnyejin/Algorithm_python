def dfs(field, start_node):
    global visit
    stack = [start_node]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while stack:
        node = stack.pop()
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= len(field) or ny >= len(field[0]): continue
            if visit[nx][ny] == 0 and field[nx][ny] == 1:
                visit[nx][ny] = 1
                stack.append([nx, ny])
    # return


def solution():
    global visit
    t = int(input())
    for case in range(t):
        m, n, k = map(int, input().split())  # 가로, 세로, 배추개수
        field = [[0] * m for _ in range(n)]
        visit = [[0] * m for _ in range(n)]
        answer = 0

        for _ in range(k):
            x, y = map(int, input().split())
            field[y][x] = 1

        for i in range(n):
            for j in range(m):
                if visit[i][j] == 0 and field[i][j] == 1:
                    dfs(field, [i, j])
                    answer += 1
        print(answer)


visit = []
solution()