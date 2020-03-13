def solution(phone_book):
    answer = True

    # 접두어가 있으면 false, 그렇지 않으면 true
    phone_book.sort()
    print(phone_book)

    temp = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i][:len(temp)] == temp:
            answer = False
            return answer

    return answer