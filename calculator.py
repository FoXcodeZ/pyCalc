# Simple Calculator
# Marcin 'FoXcodeZ' Grabowy

# PROGRAM FLOW:
# 1. Ask user for a first number.
# 2. Check the first number. Close the program is a number is invalid.
# 3. Ask user for an operator
# 4. Ask user for a second number
# 5. Make a calculation
# 6. Show the results.

# Exclamation: In python all input data is presented as strings, so we must
# convert them to floats before passing them to the calc function.

from termcolor import colored


# Return True if conversion to float is successful, otherwise return False.
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# Force conversion from string to float without checking a correctness of this conversion.
def convert_number(string):
    return float(string)


# Return True if the operator is valid, or False otherwise.
def is_valid_operator(operator):
    valid_operators = ['+', '-', '*', '/']
    for valid in valid_operators:
        if operator == valid:
            return True
    return False


# When force_valid input = True, then return valid number, ask for valid number if is not provided.
# When force_valid input = False, then return a number, or return None if number is not provided.
def ask_for_a_number(force_valid_input):
    if force_valid_input:
        while True:
            number = input("Provide a number: ")
            if is_number(number):
                return convert_number(number)
            else:
                print(f"{colored('This is not a number. Try again', 'yellow')}")
    else:
        number = input("Provide a number: ")
        if is_number(number):
            return convert_number(number)
        else:
            return None


# If force_valid_input is True, then return valid operator, of keep asking for valid operator if is not provided.
# If force_valid_input is False, then return operator if is valid, otherwise return None.
def ask_for_an_operator(force_valid_input):
    if force_valid_input:
        while True:
            operator = input("Provide an operator (+, -, *, /, **, %): ")
            if is_valid_operator(operator):
                return operator
            else:
                print(f"{colored('Invalid operator. Try again.', 'yellow')}")
    else:
        operator = input("Provide an operator (+, -, *, /, **, %): ")
        if is_valid_operator(operator):
            return operator
        else:
            return None


def calc(operator, a, b):
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None

    result = None

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b != 0:
            result = a / b
        else:
            print(f"{colored('Error!: Division by zero', 'red')}")
            return None
    elif operator == '**':
        result = a ** b
    elif operator == '%':
        result = a % b

    return result


# Main logic of the program.
def simple_calculator():
    # 1. Ask user for a first number.
    first_number = ask_for_a_number(False)

    # 2. Check the first number. Close the program is a number is invalid.
    if first_number is None:
        return

    # 3. Ask user for an operator
    operator = ask_for_an_operator(True)

    # 4. Ask user for a second number
    second_number = ask_for_a_number(True)

    # 5. Make a calculation
    result = calc(operator, first_number, second_number)

    # 6. Show the results.
    result_text = f"RESULT: {first_number} {operator} {second_number} = {result}"
    print(f"{colored(result_text, 'blue')}")


# If this is a main script, run the function: "simple_calculator()"
# It's useful for testing, when we can import this script to another script
# without running any functions (only this called from another script)
if __name__ == '__main__':
    simple_calculator()
