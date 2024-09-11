"""#task 2.1
msg = "Something went wrong"
#msg.lower()
msg = msg.lower()
print(msg)"""

#task 2.2
sms = "tutu on the tuki-kata"
result = sms.replace('tu','ta')
print(result)
#Ceci m'a permis de remplacer tous les "tu" en 'ta'

#task 2.3
string = "hello world"
position = string.find("")
print(position)
# Je dirais que  pour ce cas "a" n'est pas présent"""
for i in range(len(string)):
    if string [i]=='l':
        print(i)
        break
    else :
        pass

#task 2.4
p = 'abcdefghij'
print(p[::-2][:5][::-1][3:])
#hj   
