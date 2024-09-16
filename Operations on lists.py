import time

#Task 2.1
def multiplyList(list):
    list = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
    result = 1
    for i in range(0,len(list)):
        result = result * list[i]
    return result
print(multiplyList(list))

#Task 2.2_this code add 10 to all elements of this list
print([x + 10 for x in [3, 2, 6, 7, 1, 4]])

#Task 2.3_ce code multiplie chaque élément de la liste par chaque élément de la liste. 
print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))

#Task 2.4
x = [3, 2, 6, 7, 1, 4]
print(min(x))
print(max(x))
print()

#Task 2.5
for i in x:
    if i < 7:
        print(i)
    break

#Task 2.6
print(sorted(x, reverse = True))

#Task 2.7_ce code divise par 2 tous les éléments de la liste.
print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
print()

#Task 2.8_ ce code montre tous les éléments supérieurs à 10.
print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))

#Task 2.9_ ce code montre (index, item)
print([*enumerate([42, 3, 4, 18, 3, 10])])

#Task 2.10 "zip ==< parallélise, "
first_name = ["Jackie", "Bruce", "Arnold", "Sylvester"]
last_name = ["Stallone", "Schwarzenegger", "Willis", "Chan"]

magic = [*zip(first_name, last_name[::-1])]

print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])

#Challenge
startingTime = time.time()
import random

i = random.sample(range(1,1000000),100000)
print(i)

duration = time.time() - startingTime
print(duration)


