def dfs(start_node):
    global visit, graph
    print(start_node, "visit", visit, "graph", graph)
    visit[start_node[0]][start_node[1]] = 1
    stack = [start_node]

    while stack:
        node = stack


def solution():
    global visit, graph
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and graph[i][j] == 1:
                dfs([i, j])
                print("main", graph)

    return


visit = []
graph = []
print(solution())