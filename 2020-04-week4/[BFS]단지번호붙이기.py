def bfs(house, start_node):
    global visit
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 1
    queue = [start_node]
    visit[start_node[0]][start_node[1]] = 1

    while queue:
        node = queue.pop(0)

        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= len(house) or ny >= len(house): continue
            if visit[nx][ny] == 0 and house[nx][ny] == 1:
                queue.append([nx, ny])
                cnt += 1
                visit[nx][ny] = 1
            print(start_node, queue, cnt)
    return cnt


def solution():
    global visit
    n = int(input())
    house = [list(map(int, input())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    answer = []

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and house[i][j] == 1:
                answer.append(bfs(house, [i, j]))

    print(len(answer))
    answer.sort()
    for ans in answer: print(ans)


visit = []
solution()