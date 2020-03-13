for case in range(1, 11):
    length = int(input())
    arr = [input() for _ in range(8)]
    answer = 0

    # 가로 탐색
    for i in range(8):
        for j in range(8):
            if j + length > 8:
                break
            palindrome = arr[i][j:j+length]
            mid = len(palindrome) // 2
            # print(mid, palindrome[:mid], (palindrome[:mid-1:-1] if len(palindrome) % 2 == 0 else palindrome[:mid:-1]))
            if palindrome[:mid] == (palindrome[:mid-1:-1] if len(palindrome) % 2 == 0 else palindrome[:mid:-1]):
                answer += 1

    # 세로
    for i in range(8):
        for j in range(8):
            if i + length > 8:
                break
            palindrome = ""
            for k in range(i, i + length):
                palindrome += arr[k][j]

            mid = len(palindrome) // 2
            # print(mid, palindrome[:mid], palindrome[:mid-1:-1])
            if palindrome[:mid] == (palindrome[:mid-1:-1] if len(palindrome) % 2 == 0 else palindrome[:mid:-1]):
                answer += 1

    print("#%d" % case, answer)