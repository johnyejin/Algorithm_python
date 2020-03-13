def divisor(num):
    li = []
    for i in range(1, num + 1):
        if num % i == 0:
            li.append(i)
    return li


def solution(brown, red):
    div = divisor(red)

    if len(div) % 2 == 1:
        div.insert(len(div) // 2, div[len(div) // 2])

    for i in range(len(div) // 2):
        a = div[i]
        b = div[len(div) - i - 1]
        if (a + b + 2) * 2 == brown:
            return [b + 2, a + 2]
