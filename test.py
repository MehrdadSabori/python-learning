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
# products = ["laptop", "mouse", "keyboard", "monitor"]

# for i in range(1, 4):

#     userProduct = input('enter your product: ')

#     if userProduct in products:
#         print('product is available')
#     else:
#         print('product is not available')
# ----------------------------
# user = {
#     'name':'mehrdad',
#     'age' : 28,
#     'city': 'tehran'
# }

# print(user['name'], user['age'])

# if 'phone' in user:
#     print(user['phone'])
# else:
#     print('phone number not registered')

# user['phone'] = '090398'
# print(user['phone'])
# --------------------------------
# inputName = input('enter your name: ')
# inputAge = int(input('enter your age: '))
# inputcity = input('enter your city: ')

# user = {
#     'name' : inputName,
#     'age' : inputAge,
#     'city' : inputcity
# }

# inputPhone = input('do you have a phone? ')

# if inputPhone == 'yes':

#     inputNumber = input('enter your phone: ')

#     user['phone'] = inputNumber


# elif inputPhone == 'no':
#     pass

# for key, value in user.items():
#     print(key, value)
# -------------------------------------
# product1 = ['mouse', 'keyboard', 'monitor', 'case', 'cable']

# inputProduct = input('enter your product: ')

# def check_products(products, product):
    
#     if product in products:

#         return 'product is available'
#     else:
#         return 'product is not available'
    
# result = check_products(product1, inputProduct)
# print(result)
# -------------------------
products = {
    'mouse' : 3,
    'monitor' : 0,
    'case' : 6
}
inputUser = input('enter name product: ')

def check_product(product, inputValue):
    
    if inputValue in product:
      
        if product[inputValue] != 0:
       
            return f"{inputValue} is avalibale {product[inputValue]} in stock"
    
        elif product[inputValue] == 0:
        
            return f"{inputValue} is out of stock"
    else:
        return 'product not found'

result = check_product(products, inputUser)

print(result)