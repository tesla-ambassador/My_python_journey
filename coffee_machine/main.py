# Print report
# Check if resources are sufficient
# Process coins
# Check if transaction is successful
# Make Coffee

from menu import MENU

resources = {
    "water": "300ml",
    "milk": "250ml",
    "coffee": "100g",
    "money": "$0"
}

coins = {
    'pennies': '0.01',
    'nickels': '0.05',
    'dimes': '0.10',
    'quarters': '0.25'
}

def convert_digit(string):
    st_list = [st for st in string]
    num = float(('').join([num for num in st_list if num.isdigit() == True]))
    return num

def make_coffee():
    should_continue = True
    cash_stored = 0
    while should_continue:
        choice = input('What would you like to drink? 🥺: ').lower()
        if choice == 'espresso' or choice == 'cappuccino' or choice == 'latte':
            total_cash = 0
            change = 0
            sufficient = True

            # Check if resources are sufficient.
            for i in resources:
                if i in MENU[choice]['ingredients']:
                    if convert_digit(resources[i]) < int(MENU[choice]['ingredients'][i]):
                        print(f'You do not have enough {i}')
                        sufficient = False
                        break
            if sufficient == True:
                # Process coins
                coin_list = ['pennies', 'nickels', 'dimes', 'quarters']
                user_coins = {}

                for i in coin_list:
                    user_input = int(input(f'how many {i}?: '))
                    user_coins[i] = user_input

                for coin in user_coins:
                    total_cash += round((user_coins[coin] * convert_digit(coins[coin]))/100, 2)

                # Check if transaction is successful
                if total_cash >= MENU[choice]['cost']:
                    change = round(total_cash - MENU[choice]['cost'], 2)
                    cash_stored += round(total_cash - change, 2)
                    resources['money'] = '$' + str(cash_stored)
                    # Make coffee
                    for i in resources:
                        if i in MENU[choice]['ingredients']:
                            difference = convert_digit(resources[i]) - int(MENU[choice]['ingredients'][i])
                            if i == 'coffee':
                                resources[i] = str(int(difference)) + 'g'
                            else:
                                resources[i] = str(int(difference)) + 'ml'

                    print(f'Here is ${change} change')
                    print('Enjoy your coffee ☕️')
                else:
                    print('This is not enough money. Money refunded')
        elif choice == 'report':
            for resource in resources:
                print(f'{resource}: {resources[resource]}')
        elif choice == 'off':
            should_continue == False
            return
        else:
            print('Invalid Choice')
            return
        
make_coffee()