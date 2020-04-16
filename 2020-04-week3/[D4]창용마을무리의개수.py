def dfs(graph, start):
    visit = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit


t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    graph = {}
    visit = []
    answer = 0

    # 그래프 만들기
    for i in range(m):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]
    print(graph)

    for key in graph.keys():
        if key in visit:
            continue
        else:
            visit.extend(dfs(graph, key))
            answer += 1

    answer += n - len(graph)  # 아는 사람이 아예 없는 아싸도 있으니까ㅠㅠ
    print("#%d" % case, answer)