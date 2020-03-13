def solution(record):
    answer = []
    res = []
    dic = {}  # {id: 닉네임}

    for i in range(len(record)):
        temp = record[i].split(' ')

        if temp[0] == 'Enter':
            dic[temp[1]] = temp[2]
            res.append([temp[0], temp[1]])
        elif temp[0] == 'Leave':
            res.append([temp[0], temp[1]])
        else:
            dic[temp[1]] = temp[2]

    for i in range(len(res)):
        if res[i][0] == 'Enter':
            string = dic[res[i][1]] + "님이 들어왔습니다."
            answer.append(string)
        else:
            string = dic[res[i][1]] + "님이 나갔습니다."
            answer.append(string)

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])