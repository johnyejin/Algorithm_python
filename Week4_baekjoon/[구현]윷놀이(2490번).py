# 배 = 0, 등 = 1
for case in range(3):
    temp = list(map(int, input().split()))
    cnt = temp.count(0)

    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    else:
        print('E')