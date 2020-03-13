n = int(input())
arr = []

for case in range(n):
    a, b, c, d = input().split()
    arr.append([int(b), int(c), int(d), a])

arr = sorted(arr, key=lambda x: (-x[0], x[1], -x[2], x[3]))
for line in arr:
    print(line[3])