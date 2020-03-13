def mergeSort(x):
    if len(x) > 1:
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if int(lx[li] + rx[ri]) > int(rx[ri] + lx[li]):
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))  # str 리스트로 바꿔주기

    mergeSort(numbers)

    answer = ''.join(numbers)

    if int(answer) == 0: answer = '0'

    return answer