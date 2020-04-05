# 트랜잭션에 중복 있음!!
# 스냅샷에 존재하지 않는 계좌가 있을 수 있음!!
def solution(snapshots, transactions):
    answer = []
    dic = dict()
    id = []

    for snap in snapshots:
        dic[snap[0]] = int(snap[1])

    for tran in transactions:
        if tran[0] in id:
            continue
        id.append(tran[0])
        if tran[1] is "SAVE":
            if tran[2] in dic:
                dic[tran[2]] += int(tran[3])
            else:
                dic[tran[2]] = int(tran[3])
        elif tran[1] is "WITHDRAW":
            dic[tran[2]] -= int(tran[3])

    for key, value in dic.items():
        answer.append([key, str(value)])

    answer.sort()
    return answer


print(solution([
["ACCOUNT2", "100"],
["ACCOUNT1", "150"]],
[["1", "SAVE", "ACCOUNT2", "100"],
["2", "WITHDRAW", "ACCOUNT1", "50"],
["1", "SAVE", "ACCOUNT2", "100"],
["4", "SAVE", "ACCOUNT3", "500"],
["3", "WITHDRAW", "ACCOUNT2", "30"]]))
# result
# [["ACCOUNT1", "50"],
#  ["ACCOUNT2", "220"],
#  ["ACCOUNT3", "500"]]