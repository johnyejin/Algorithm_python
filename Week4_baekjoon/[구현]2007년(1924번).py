monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

month, day = map(int, input().split())

sumDay = sum(monthList[0:month-1]) + day - 1

print(dayList[sumDay % 7])