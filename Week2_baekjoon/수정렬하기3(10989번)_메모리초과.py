n = int(input())
num_list = []
for i in range(n):
    temp = int(input())
    num_list.append(temp)

num_list.sort()

for i in num_list:
    print(i)