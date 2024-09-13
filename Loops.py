"""#Example_:for i in range(-10,10):
    print(i)
# ça va de -10 à 10"""

"""#Task 2.1
a = 1
b = 1000
for i in range (0,999):
    a = a + 1
    print(a)"""

"""#Task 2.2
user = input('Write a sentence:')
for i in user:
    x = i * 2
    print(x, end = "")"""

#Task 2.3
"""for i in range (10000, 0, -1):
    if i % 7 == 0:
        print(i)"""

#Task 2.4
"""for i in range (-30, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)"""

"""#Task 2.5
for i in range(99, 0, -1):
    if i == 1:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.Take one down and pass it around, {i} bottles of beer on the wall")
    else :
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.Take one down and pass it around, {i-1} bottles of beer on the wall")
print("No more beers on the wall, no more bottles of beer")"""

"""#Task 2.6
n = int(input())
for i in range(2, n // 2 + 1):
    multiples = [j for j in range (1, n-1, i-1) if j % i ==0]
    if multiples:
        print(multiples)"""

# Chercher dans ton input (y) chaine de caractère => si aeiou est présent, et dans ce cas tu affiches le nombre
# En dehors de ta boucle, tu fais les autres questions de l'énoncé

# dans mon input je cherche si, "a" est présent, puis je cherche si "e" est présent...

#Challenge
def inputfunc():
    x = int(input())
    y = input()
    exit
    for char in y:
        if char in "aeiou":
            print(x)
        else :
            print(y)
inputfunc()