m = 2147483647
a = 2147483629
c = 2147483587

seed = int(input('please enter a 4-digit number:\n'))
number = seed
alreadyset = set()
i = 0

while number not in alreadyset:
    print(number, end = ' ')
    alreadyset.add(number)
    number = (a * number + c) % m
    i = i + 1
    if (i>=100):
        break
