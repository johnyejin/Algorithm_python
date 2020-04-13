def mergeSort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        lx, rx = numbers[:mid], numbers[mid:]
        mergeSort(lx)
        mergeSort(rx)

        left, right, i = 0, 0, 0
        while left < len(lx) and right < len(rx):
            if int(lx[left] + rx[right]) > int(rx[right] + lx[left]):
                numbers[i] = lx[left]
                left += 1
            else:
                numbers[i] = rx[right]
                right += 1
            i += 1
        numbers[i:] = lx[left:] if left != len(lx) else rx[right:]

def solution(numbers):
    numbers = list(map(str, numbers))
    mergeSort(numbers)
    answer = ''.join(numbers)

    if int(answer) == 0: answer = '0'

    return answer


# print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330