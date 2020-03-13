burger = []
drink = []
for i in range(3):
    temp = int(input())
    burger.append(temp)
for i in range(2):
    temp = int(input())
    drink.append(temp)

cheap = min(burger) + min(drink) - 50

print(cheap)