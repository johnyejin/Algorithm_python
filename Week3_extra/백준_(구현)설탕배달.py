n = int(input())

five = n // 5
rest = n - five * 5
while True:
    print(five, rest)
    if rest % 3 == 0:
        print(five + (rest // 3))
        break

    if five == 0 and rest % 3 != 0:
        print(-1)
        break

    if five != 0:
        five -= 1
        rest = n - five * 5
