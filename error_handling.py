#using print() and f-strings
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result

#Using python built-in debugging module
import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))

#exceptions
try: #the block of code where error might occur
    x = 10 / 0
except ZeroDivisionError: #runs if an error of soecified type is raised inside try
    print("You can't divide by zero!")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else: #run if no exceptionis raised in the try block
    print('Division successful:', x)
finally: #runs no matter what, if an exception occurs or not. useful for clean-up tasks
    print('This block always runs.')

#can catch multiple exceptions with separate except blocks; making error responses more specific and useful
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
#can catch multiple exceptions in a single except clause
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')

#raise statement allows to trigger manual exceptions in the code, allowing to create custo error messages
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}')

#without any argument, raise statement re-raises the current exception being handled
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')
# can create and raise custom exceptions by defining your own exception classes
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')

#raise statement can also be used with the from keyword to chain exceptions, showing the relationship between different errors
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')

#you can use assert instead of raise
def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')
