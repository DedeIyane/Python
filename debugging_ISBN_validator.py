def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{isbn} code should be {length} digits long.')
        return
    main_digits = isbn[0:length]
    given_check_digit = isbn[length]
    main_digits_list = [int(digit) for digit in main_digits]
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')
def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')
    isbn = values[0]
    length = int(values[1])
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

main()


#corrected code
def validate_isbn(isbn, length):
    isbn = str(isbn)
    length = int(length)
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    main_digits = isbn[0:length-1]
    given_check_digit = isbn[length -1]
    main_digits_list = [int(digit) for digit in main_digits]
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')
def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
def main():
    user_input = input('Enter ISBN and length: ')

    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')

    if not values[1].isdigit():
        print('Length must be a number.')
        return

    isbn = values[0]
    length = int(values[1])
    if not isbn[:-1].isdigit() or (not isbn[-1].isdigit() and isbn[-1] != 'X'):
        print('Invalid character was found.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

#main()

validate_isbn(1530051126,10)


#my cleaner version
def calculate_check_digit_10(isbn):
    total = 0

    for i in range(9):
        total += (i + 1) * int(isbn[i])

    remainder = total % 11

    if remainder == 10:
        return 'X'

    return str(remainder)


def calculate_check_digit_13(isbn):
    total = 0

    for i in range(12):
        digit = int(isbn[i])

        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    remainder = total % 10
    result = (10 - remainder) % 10

    return str(result)


def validate_isbn(isbn, length):

    if length == 10:

        if len(isbn) != 10:
            print('ISBN-10 code should be 10 digits long.')
            return

        if not isbn[:-1].isdigit() or (isbn[-1] != 'X' and not isbn[-1].isdigit()):
            print('Invalid character was found.')
            return

        expected = calculate_check_digit_10(isbn)

        if isbn[-1] == expected:
            print('Valid ISBN Code.')
        else:
            print('Invalid ISBN Code.')

    elif length == 13:

        if len(isbn) != 13:
            print('ISBN-13 code should be 13 digits long.')
            return

        if not isbn.isdigit():
            print('Invalid character was found.')
            return

        expected = calculate_check_digit_13(isbn)

        if isbn[-1] == expected:
            print('Valid ISBN Code.')
        else:
            print('Invalid ISBN Code.')


def main():
    user_input = input('Enter ISBN and length: ')

    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')

    if len(values) != 2:
        print('Enter comma-separated values.')
        return

    isbn = values[0]
    length_value = values[1]

    if not length_value.isdigit():
        print('Length must be a number.')
        return

    length = int(length_value)

    if length not in (10, 13):
        print('Length should be 10 or 13.')
        return

    validate_isbn(isbn, length)


if __name__ == "__main__":
    main()