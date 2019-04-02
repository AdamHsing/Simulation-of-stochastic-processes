n = 2147483647
g = 16807
seed = int(input('please enter a 4-digit number:\n'))
number = seed
alreadyset = set()
i = 0

while number not in alreadyset:
    print(number, end = ' ')
    alreadyset.add(number)
    number = g * number % n
    i = i + 1
    if (i>=100):
        break
