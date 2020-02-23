def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))  # str 리스트로 바꿔주기

    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if int(numbers[i] + numbers[j]) < int(numbers[j] + numbers[i]):
                numbers[i], numbers[j] = numbers[j], numbers[i]

    answer = ''.join(numbers)
    return answer