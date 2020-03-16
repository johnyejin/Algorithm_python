# 1번 장대에 있는 원판들을 그대~로 3번 장대로 옮겨야함
def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)  # n-1개 원판을 2번으로 옮긴 후 맨 밑의 원판을 1번->3번으로 옮김
    else:
        hanoi(disk - 1, start, end, mid)
        print(start, end)  # n-1개 원판을 1번->2번으로 옮김
        hanoi(disk - 1, mid, start, end)  # 이후 다시 n-1개 원판을 2번->3번으로 옮김


n = int(input())
total = 0
for _ in range(n):
    total = total * 2 + 1

print(total)
hanoi(n, 1, 2, 3)