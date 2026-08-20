products = {
    "mouse": 3,
    "keyboard": 5,
    "monitor": 0,
    "case": 2
}

Menu = '1.show products \n2.check product \n3.Buy product \n4.add product \n5.Exit'

def show_products(product):
    
    for key, value in product.items():
        print(key, value)

def check_product(product, productName):
    
    if productName in product:
        if product[productName] == 0 :

            return 'product is out of stock'

        else:

            return f'{productName} is available {product[productName]} in stock'
    else:
        return 'product not found'

def Buy_Product(product, productName, productNumber):


    if productName in product:

        if product[productName] == 0:

            print('product is out of stock')

        else:

            if product[productName] >= productNumber:
                print('succesful')
                product[productName] -= productNumber
            else:
                result = f'The number of {productName} in stock is low. There are {product[productName]} {productName} in stock'
                print(result)

    else:
        print('invalid product name')

def add_Product(product, productName, productNumber):
    
    if productName in product:
        store = f'There is a {productName} in the store'
        print(store)
    else:
        print('succesful')
        product[productName] = productNumber
        
        
        

while True:

    try:
        print(Menu)
        inputMenuNumber = int(input('Enter Menu number: '))

        if inputMenuNumber == 1:
            resultShowProduct = show_products(products)
            print(resultShowProduct)
            
        elif inputMenuNumber == 2:
            inputProductName = input('Enter product name: ')
            resultCheck = check_product(products, inputProductName)
            print(resultCheck)
        
        elif inputMenuNumber == 3:
                inputProductName = input('Enter product name: ')
                inputQuantity = int(input('Enter quantity: '))
                resultBuy = Buy_Product(products, inputProductName, inputQuantity)
                print(resultBuy)
                
                
        elif inputMenuNumber == 4:
            inputProductName = input('Enter product name: ')
            inputQuantity = int(input('Enter quantity: '))
            add_Product(products, inputProductName, inputQuantity)
            

        elif inputMenuNumber == 5:
            print('goodbye!')
            break
            
        
            

    except ValueError:
        print('invalid number')
        continue
