# stack 뒤에 넣을 수 있으면 해당 idx 반환하고, 넣을 수 있는게 없으면 False 반환
def check(stack, location):
    for i in range(len(stack)):
        if len(stack[i]) == location:
            return i
    return False


t = int(input())
for case in range(1, t+1):
    flog = input()
    max_cnt = 0
    stack = []
    cnt = 0

    for i in range(len(flog)):
        if flog[i] is 'c':
            stack.append(['c'])
            cnt += 1
            if cnt > max_cnt: max_cnt = cnt
        elif flog[i] is 'r':
            temp = check(stack, 1)
            if temp is False:
                max_cnt = -1
                break
            stack[temp].append('r')
        elif flog[i] is 'o':
            temp = check(stack, 2)
            if temp is False:
                max_cnt = -1
                break
            stack[temp].append('o')
        elif flog[i] is 'a':
            temp = check(stack, 3)
            if temp is False:
                max_cnt = -1
                break
            stack[temp].append('a')
        elif flog[i] is 'k':
            temp = check(stack, 4)
            if temp is False:
                max_cnt = -1
                break
            stack[temp].append('k')
            stack.pop(0)
            cnt -= 1
        # print(stack)

    if len(stack) != 0: max_cnt = -1
    print("#%d" % case, max_cnt)