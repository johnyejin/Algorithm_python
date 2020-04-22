def bfs(maze, n, m):
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    queue = [[0, 0, 1]]  # [x, y, distance]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        node = queue.pop(0)
        if node[:2] == [n-1, m-1]: return node[2]

        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visit[nx][ny] == 0 and maze[nx][ny] == 1:
                queue.append([nx, ny, node[2]+1])
                visit[nx][ny] = 1
        # print("visit", visit, "queue", queue, answer)


def solution():
    n, m = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(n)]

    print(bfs(maze, n, m))


solution()