numbers = [2, 2, 4, 5, 1, 5]
start_index = 0
list_length = len(numbers)
for number in numbers:
    for i in range(start_index, list_length):
        if numbers[start_index] == numbers[i]:
            del numbers[start_index]
            list_length-=1
            break
    start_index+=1

print(numbers)