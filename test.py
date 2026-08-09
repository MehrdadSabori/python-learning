# userName = input("enter your name: ")
# userAge = int(input("enter your age: "))
# yourBirthday = 2026 - userAge
# print(userName, userAge, yourBirthday)
# --------------------
# yourAge = int(input('enter your age: '))
# if yourAge <= 12:
#     print('child')
# elif yourAge <= 17:
#     print('teenager')
# else:
#     print('adult')
# ------------------
# for number in range(1, 21):
#     if number % 2 == 0:
#         print(number)
# -------------------
# number = 1
# while number <= 5:
#     print(number)
#     number = number + 1
# --------------------
helpUser = '1.show number even' \
'2.show number odd' \
'3.exite'
userNumber = int(input('enter your number: '))
if userNumber == 1:
    for numbers in range(1, 11):
        numbers % 2 == 0
        print(numbers)
elif userNumber == 2:
    for numbers in range(1, 10):
        numbers % 2 == 1
        print(numbers)
else:
    print('invalid choice')    