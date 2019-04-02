seed = int(input('please enter a 4-digit number:\n'))
number = seed
alreadyset = set()

while number not in alreadyset:
    print(number, end = ' ')
    alreadyset.add(number)
    number = int(str(number ** 2).zfill(6)[2:6])
