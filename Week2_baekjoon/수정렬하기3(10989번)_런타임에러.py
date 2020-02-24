n = int(input())
num_list = [0] * 10001
for i in range(n):
    temp = int(input())
    num_list[i] = temp

num_list.sort()

for i in num_list:
    if i is 0:
        continue
    print(i)