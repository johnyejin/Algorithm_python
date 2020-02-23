def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))  # str 리스트로 바꿔주기
    max_numbers = []

    while len(numbers) != 0:
        max_numbers.append(max(numbers))
        print(max(numbers))
        numbers.remove(max(numbers))

    return answer