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
# helpUser = "1.show number even \n2.show number odd \n3.exit"
# while True:
#     print(helpUser)
#     userNumber = int(input("enter your number: "))
#     if userNumber == 1:
#         for numbers in range(1, 11):
#             if numbers % 2 == 0:
#                 print(numbers)
#     elif userNumber == 2:
#         for numbers in range(1, 11):
#             if numbers % 2 == 1:
#                 print(numbers)
#     elif userNumber == 3:
#         print('exite')
#         break
#     else:
#         print('invalid choice')
# ------------------------------------
# products = []

# for shop in range(1,4):
#     shopList = input('Enter your product list: ')
#     products.append(shopList)

# for product in products:
#     print(product)
# ---------------------------------------
products = ["laptop", "mouse", "keyboard", "monitor"]

for i in range(1, 4):

    userProduct = input('enter your product: ')
    
    if userProduct in products:
        print('product is available')
    else:
        print('product is not available')