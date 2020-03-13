 # 1번노드와 가장 멀리 떨어진 노드의 개수 구하기
def bfs(start):
    global graph
    visit = list()
    lengthQueue = list()  # [1부터 거리]
    queue = list()  # [노드]
    maxLength, ans = 0, 0

    lengthQueue.append(0)
    queue.append(start)

    while lengthQueue:
        node = queue.pop(0)
        cnt = lengthQueue.pop(0)

        if node not in visit:
            visit.append(node)
            # queue.extend(graph[node])
            for i in range(len(graph[node])):
                if graph[node][i] not in visit and graph[node][i] not in queue:
                    queue.append(graph[node][i])
                    lengthQueue.append(cnt+1)

        print(lengthQueue, queue, visit)
        if len(lengthQueue) == 0:
            return ans

        curLength = max(lengthQueue)
        cntLength = lengthQueue.count(curLength)
        if maxLength < curLength or ans < cntLength:
            maxLength = curLength
            ans = cntLength

    return ans


def solution(n, edge):
    global graph
    answer = 0

    # 일단, edge를 graph(딕셔너리)로 바꾸기
    for i in range(len(edge)):
        if edge[i][0] in graph:
            graph[edge[i][0]].append(edge[i][1])
        else:
            graph[edge[i][0]] = [edge[i][1]]

        if edge[i][1] in graph:
            graph[edge[i][1]].append(edge[i][0])
        else:
            graph[edge[i][1]] = [edge[i][0]]
    print(graph)

    # {1: [[2, 0], [3, 0]]} 오른쪽 0은 1과 떨어진 거리
    # bfs에서 노드 pop하고 append 할때마다 +1 해주기
    answer = bfs(1)

    return answer


graph = {}
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))