import os

path = "/Users/preetinarayanan/Desktop/AdventOfCode"
os.chdir(path)

file_name = 'day1.txt'

with open(file_name) as f:
    lines = f.readlines()

elf = 1
sum_calories = 0
first_max_calories = 0
second_max_calories = 0
third_max_calories = 0
elf_with_max_calories = 0
for line in lines:
    if line == '\n':
        if sum_calories > first_max_calories:
            first_max_calories, second_max_calories,third_max_calories = sum_calories,first_max_calories,second_max_calories
            print('Max calories are carried by elf ' + str(elf) + ' which is ' + str(first_max_calories))
        elif sum_calories > second_max_calories and sum_calories <= first_max_calories:
            second_max_calories,third_max_calories = sum_calories,second_max_calories
            print('Second max calories are carried by elf ' + str(elf) + ' which is ' + str(second_max_calories))
        elif sum_calories > third_max_calories and sum_calories <= second_max_calories:
            third_max_calories = sum_calories
            print('Third max calories are carried by elf ' + str(elf) + ' which is ' + str(third_max_calories))
        elf += 1
        sum_calories = 0
    else:
        sum_calories += int(line)

total_calories = first_max_calories + second_max_calories + third_max_calories
print(total_calories)



