from calc_art import logo
import os

clear = lambda: os.system('clear')

print(logo)
input_1 = float(input('Please enter the first number: '))
operator_1 = input('Please choose one of the following:\n+\n-\n*\n/\n%\n\n')
input_2 = float(input('Please enter the second number: '))

def calculate(num1, num2, operator):
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2
    elif operator == '%':
        answer = num1 % num2
    else:
        return 'That is an invalid operand'
    print(f'The answer is {answer}')
    continue_prompt = input('Do you want to continue with current answer? (y) or (n): ').lower()
    if continue_prompt == 'y':
        clear()
        operator_2 = input('Please choose one of the following:\n+\n-\n*\n/\n%\n\n')
        input_3 = float(input('Please enter the second number: '))
        new_answer = calculate(num1=answer, num2=input_3, operator=operator_2)
        return new_answer
    else:
        return answer

calculation = calculate(num1=input_1, num2=input_2, operator=operator_1)
print(calculation)