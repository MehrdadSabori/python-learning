# userName = input("enter your name: ")
# userAge = int(input("enter your age: "))
# yourBirthday = 2026 - userAge
# print(userName, userAge, yourBirthday)
# --------------------
yourAge = int(input('enter your age: '))
if yourAge <= 12:
    print('child')
elif yourAge <= 17:
    print('teenager')
else:
    print('adult')