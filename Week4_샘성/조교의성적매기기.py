t = int(input())
grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for case in range(t):
    n, k = map(int, input().split())  # n은 항상 10의 배수
    arr = []

    for i in range(n):
        a, b, c = map(int, input().split())
        total = a * 0.35 + b * 0.45 + c * 0.2
        arr.append((total, i+1))

    arr.sort()

    for i in range(n):
        if arr[i][1] == k:
            print("#%d" % (case+1), grade[(i // (n//10)) % 10])
            break