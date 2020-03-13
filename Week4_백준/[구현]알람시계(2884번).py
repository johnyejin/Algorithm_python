time, second = map(int, input().split())

if second - 45 < 0:
    if time - 1 < 0:
        time = 23
    else:
        time -= 1
    second += 15  # second + 60 - 45
else:
    second -= 45

print(time, second)