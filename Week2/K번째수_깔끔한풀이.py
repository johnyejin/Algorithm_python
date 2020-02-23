def solution(array, commands):
    answer = []

    for x, y, z in commands:
        temp = array[x - 1:y]
        temp.sort()
        answer.append(temp[z - 1])

    return answer