arr = list(map(int, input().split()))
arr.sort()
order = input()
dic = {'A': 0, 'B': 1, 'C': 2}

print(arr[dic[order[0]]], arr[dic[order[1]]], arr[dic[order[2]]])