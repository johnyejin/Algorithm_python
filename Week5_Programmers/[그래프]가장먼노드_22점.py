# 1번노드와 가장 멀리 떨어진 노드의 개수 구하기
def bfs(start):
    global graph
    visit = list()
    queue = list()  # [노드, 1부터 거리]
    q = list()  # [노드]

    queue.append([start, 0])
    q.append(start)

    while queue:
        node = queue[0][0]
        cnt = queue[0][1]
        queue.pop(0)
        q.pop(0)

        if node not in visit:
            visit.append(node)
            for i in range(len(graph[node])):
                if graph[node][i][0] not in visit and graph[node][i][0] not in q:
                    queue.append([graph[node][i][0], cnt + 1])
                    q.append(graph[node][i][0])

        print(queue, q, visit)
        if len(visit) + len(q) == len(graph):
            return len(q)


def solution(n, edge):
    answer = 0
    global graph

    # 일단, edge를 grape(딕셔너리)로 바꾸기
    for i in range(len(edge)):
        if edge[i][0] in graph:
            graph[edge[i][0]].append([edge[i][1], 0])
        else:
            graph[edge[i][0]] = [[edge[i][1], 0]]

        if edge[i][1] in graph:
            graph[edge[i][1]].append([edge[i][0], 0])
        else:
            graph[edge[i][1]] = [[edge[i][0], 0]]
    print(graph)

    # {1: [[2, 0], [3, 0]]} 오른쪽 0은 1과 떨어진 거리
    # bfs에서 노드 pop하고 append 할때마다 +1 해주기
    answer = bfs(1)
    print(answer)

    return answer


graph = {}
solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])