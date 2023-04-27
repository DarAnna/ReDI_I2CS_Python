# 1.Напишіть функцію яка повертає максимум із 3 чисел
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
#інший підхід, теж правильний
def max_of_three1(num1, num2, num3):
    max_num = max(num1, num2, num3)
    return max_num
    
#2. Напишіть програму яка друкує тільки парні числа з певного списку
nums=[1,2,3,4,5,6,7,8]
total = 0
for number in nums:
    if number % 2 == 0:
        total += number
print(total)

# 3. Напишіть програму яка сумує всі парні числа від 0 до певного числа (х). 
# Для цього створіть функцію яка має х як параметер і викличте цю функцію з числом, яке введе юзер.
def sum_even_numbers(x):
    total = 0
    for i in range(0, x+1, 2):
        total += i
    return total

user_input = int(input("Enter a number: "))
result = sum_even_numbers(user_input)
print(result)

# 4. Напишіть програму яка бере список чисел і створює новий список чисел тільки з непарними числами з першого списку
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for number in original_list:
    if number % 2 == 1:
        even_list.append(number)
print("The even numbers in the list are:", even_list)

# 5. Напишіть програму, яка отримує на вхід список чисел і виводить найбільше число з цього списку. 
# Наприклад, якщо на вході задано список [1, 4, 7, 2, 9], то на виході повинно бути 9.

numbers = [1, 4, 7, 2, 9]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)