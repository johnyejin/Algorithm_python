n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort()

length = 1000000000
for i in range(n-1):
    if abs(arr[i][0] - arr[i+1][0]) ** 2 + abs(arr[i][1] - arr[i+1][1]) ** 2 < length:
        length = abs(arr[i][0] - arr[i+1][0]) ** 2 + abs(arr[i][1] - arr[i+1][1]) ** 2

print(length)