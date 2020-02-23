n = int(input())
a = [int(x) for x in input().strip().split()]
b = [int(y) for y in input().strip().split()]
range_a = [-1 for _ in range(n)]
same_b = [-1 for _ in range(n)]
answer = 0

while True:
    if min(a) == 101:
        break

    range_a[b.index(max(b))] = min(a)
    a[a.index(min(a))] = 101
    same_b[b.index(max(b))] = max(b)
    b[b.index(max(b))] = -1

for i in range(n):
    answer += range_a[i] * same_b[i]

print(answer)