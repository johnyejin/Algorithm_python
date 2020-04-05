# 효율성 중요!!!!! 10의 5승 실화냐
# 태그를 많이 포함할수록 앞에 위치
# 태그 수가 동일할 때는 사전식 순서대로
# 상위 10건까지만 return
def solution(dataSource, tags):
    answer = []
    dic = dict()

    for data in dataSource:
        cnt = 0  # 일치하는 태그 수
        for i in range(1, len(data)):
            if data[i] in tags:
                cnt += 1
        dic[data[0]] = cnt
    print(dic)

    alignment = sorted(dic.items(), key=lambda x: (-x[1]))

    for key, value in alignment:
        if len(answer) > 10: break
        if value == 0: continue
        answer.append(key)

    return answer


print(solution(
[
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"]))
# ["doc1", "doc2", "doc4", "doc3"]