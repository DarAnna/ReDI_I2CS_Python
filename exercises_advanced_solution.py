#1. Напишіть програму, яка отримує на вхід список чисел і виводить список тих самих чисел але в зворотньому порядку. 
# Наприклад, якщо на вході задано список [5, 3, 8, 1], то на виході має бути [1, 8, 3, 5].
original_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(original_list)-1, -1, -1):
    reversed_list.append(original_list[i])
print(reversed_list)

#теж правильно
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))
print(reversed_list)

#2.Напишіть програму, яка отримує на вхід текст і виводить на екран зворотний йому рядок. 
#Наприклад, якщо на вході "hello", то на виході повинно бути "olleh".
user_input = input("Enter a string: ")
reversed_string = ""
for i in range(len(user_input)-1, -1, -1):
    reversed_string += user_input[i]
print(reversed_string)

#3. Напишіть програму, яка отримує на вхід два списки чисел і виводить спільні елементи між цими двома списками. 
# Наприклад, якщо на вході задано списки [1, 2, 3, 4] і [3, 4, 5, 6], то на виході має бути [3, 4].
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
common_elements = []
for element in list_1:
    if element in list_2:
        common_elements.append(element)
print(common_elements)

#4. Напишіть програму, яка отримує на вхід список слів і виводить кількість унікальних слів у списку.
# Наприклад, якщо вхідний список має вигляд ["apple", "banana", "apple", "cherry", "cherry", "cherry", "cherry"], то на виході повинно бути 3 (є 3 унікальних слова: "apple", "banana" і "cherry").
strings = ["apple", "banana", "apple", "cherry", "cherry", "cherry"]
unique_strings = set(strings)
number_of_unique_strings = len(unique_strings)
print(number_of_unique_strings)