n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 2:
    print(n - 1)
else:
    print(n // (k - 1) if n % (k - 1) <= 1 else n // (k - 1) + 1)
