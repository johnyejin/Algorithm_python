n = int(input())
# display = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # 각 숫자가 필요한 획수
answer = ''

while n > 5:
    n -= 2
    answer += '1'

if n == 5:
    answer += '71'
elif n == 4:
    answer += '11'
elif n == 3:
    answer += '7'
else:
    answer += '1'

print(int(answer))