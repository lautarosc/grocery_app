dict_shopping = dict()

def main():

    print(r'''
Enter an option to continue: 

1) Add a new product
2) Modify a product
3) Delete a product
4) Show shopping list
5) Exit    
    
 ''')
    
    decision = input('> ')

    while decision != '1' and decision != '2' and decision != '3' and decision != '4' and decision != '5':
        print('Invalid option. Try again:')
        decision = input('> ')


# --------------- 1) ADD NEW PRODUCT ---------------

    def new_product(): 

        decision = 'y'

        while decision == 'y':

            print('\nEnter the name of the product:')
            name_product = input('> ')
            name_product = name_product.lower()

            print('Enter the price per unit:')
            price_unit = float(input('> '))

            print('Enter how many units are you buying:')
            number_units = int(input('> '))

            dict_shopping[name_product] = [price_unit, number_units]

            print(f'\n{name_product} has been added to the shopping list')

            print('\nWould you like to add more? (y/n):')
            decision = input('> ')

            while decision != 'y' and decision != 'n':
                print('Invalid option. Try again:')
                decision = input('> ')

            if decision == 'n':
                print('---' * 10)
                main()  
                        

# --------------- 2) MODIFY PRODUCT ---------------

    def modify_product():

        print('\nEnter the name of the product you\'d like to modify')
        name_product = input('> ')
        name_product = name_product.lower()

        while name_product not in dict_shopping: 
            print('Invalid option. Try again:')
            name_product = input('> ')

        print('Enter the correct price:')
        price_unit = float(input('> '))

        print('Enter how many units are you buying:')
        number_units = int(input('> '))

        dict_shopping[name_product] = [price_unit, number_units]

        print(f'\nProduct {name_product} has been modified.')
        print('---' * 10)
        
        main()

# --------------- 3) DELETE PRODUCT ---------------

    def delete_product():

        print('Enter the name of the product to delete:')
        decision = input('> ')
        decision = decision.lower()

        while decision not in dict_shopping:
            print('Invalid option. Try again:')
            decision = input('> ')
        
        del dict_shopping[decision]

        print(f'\n{decision} has been deleted.')
        print('---' * 10)

        main()

# --------------- 4) SHOW SHOPPING LIST ---------------

    def show_list():

        final_price = 0

        for k, v in dict_shopping.items():
            print('\nProduct:', k, '\nPrice per unit: $', v[0], '\nQuantity:', v[1], '\nSubtotal: $', v[0]*v[1])

            final_price += v[0] * v[1]
        
        print('\nTotal price to pay: $', final_price)
        print('---' * 10)

        main()

# --------------- 5) EXIT PROGRAM ---------------

    def exit_app():

        print('\nThank you for using this app!')
        print('---' * 10)

        main()




    if decision == '1':
        new_product()

    elif decision == '2':
        modify_product()

    elif decision == '3':
        delete_product()

    elif decision == '4':
        show_list()

    elif decision == '5':
        exit_app()


main()















# for k,v in dict_shopping.items():
#     print(k, v)