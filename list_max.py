numbers = [3, 5, 2, 8]
max = numbers[0]

for number in numbers[1:]:
    if(number > max):
        max = number

print(max)
