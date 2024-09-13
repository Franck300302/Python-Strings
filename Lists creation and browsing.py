#Task 1.1
numbers = [1, 2, 3, 4, 5]
print(numbers[0])

#Task 1.2
print(numbers[-1])

#Task 1.3
numbers.append(6)
print(numbers)

#Task 1.4
print(numbers)

#Task 1.5
del numbers[-3]
print(numbers)

#Task 1.6
numbers.insert(0, 7)
print(numbers)

#Task 1.7
print(numbers[2:])

#Task 1.8
numbers.reverse()

#Task 1.9
print(numbers[::2])

#Task 1.10
New_list = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] 
numbers.extend(New_list)
print(numbers)

#Task 1.11
my_first_list = [4, 5, 6, ]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
print(my_first_list)
""" .extend() add my_second_list to my_first_list"""
my_first_list = [*my_first_list, *my_second_list]
print(my_first_list)
"""[*variable1, *variable2] duplique variable2 deux fois à la fin de la list variable1 """

