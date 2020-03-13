import sys

n = int(input())
num_list = [0] * 10001
for num in sys.stdin:
    num_list[int(num)] += 1

for i in range(10001):
    if num_list[i] is 0:
        continue
    for j in range(num_list[i]):
        print(i)