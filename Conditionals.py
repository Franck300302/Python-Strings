#task  1.1
a = 42 
b = 12 
print(a > b)
#True

a = 12
b = 12
print(a = b)
#error

a = 12
b = 12 
print(a == b)
#true

a = "hello"
b = "world"
print(a == b)
#false

a = 218
b = 118
print(218 >= 118)
#True

print("a".upper() == "A")
#True

a = 1 
b = 2 
c = 3 
d = 4
print(a*b*c*d <= 9) 
#False

print("z" in "azerty")
#True

#Task 1.2
a = 27 
if a == 42:
    print("Correct answer")
else:
    print("Error")

#Task 1.3
x = 127
#x=int(input("entrez un nombre: "))
if (x % 2) == 0:
    print("the integer is even")
else:
    print("the integer is odd")

#Task 1.4
Ask = input("Evrivez une phrase")
if Ask == "Open sesame":
    print("access granted")
elif Ask == "will you open, you goddamn !¤*@!":
    print("access fucking granted")
else :
    print("permission denied")


#Task 1.5
x = int(input("Entrez un nombre: "))
if x == 42:
    print('OK')
elif x <= 21:
    print("OK")
elif (x % 2) == 0 :
    print("OK")
elif (x / 2) < 21 :
    print("OK")
elif (x % 2) >= 45:
    print('OK') 
else :
    print("You got wrong my poor friend!")

#Task 1.6 
a = 42
b = 41 
if a == b :
    print("A and B are the sames") 
elif b <= a :
    print("B is equal or lower as A")
elif b != a :
    print('B is different from A')
else : 
    pass
