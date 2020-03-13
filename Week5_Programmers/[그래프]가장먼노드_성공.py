from collections import defaultdict, deque


# 1번노드와 가장 멀리 떨어진 노드의 개수 구하기
def bfs(graph, start):
    visit = set()
    queue = deque()  # (노드, 거리)
    queue.append((start, 0))
    visit.add(start)
    cntDic = defaultdict(lambda: 0)  # 각 거리별 노드의 개수

    while queue:
        node, cnt = queue.popleft()
        visit.add(node)
        for i in graph[node]:
            if i not in visit:
                visit.add(i)
                queue.append((i, cnt+1))
                cntDic[cnt + 1] += 1
        print(queue, visit, cnt, cntDic.items())

    return cntDic[cnt]


def solution(n, edge):
    graph = defaultdict(set)
    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)

    answer = bfs(graph, 1)

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))