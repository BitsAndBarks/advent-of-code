import re

file_name = "input.txt"


def find_digits(s):
    # find all digits in the string
    digits = re.findall(r'\d', s)

    # if no digits are found, return two zeroes
    if not digits:
        return [0, 0]

    # if only one digit is found, return it twice as integers
    if len(digits) == 1:
        return [int(digits[0]), int(digits[0])]

    # otherwise, return the first and last digit as integers
    return [int(digits[0]), int(digits[-1])]


def sum_of_numbers(input_file):
    total_sum = 0
    with open(input_file, 'r') as file:
        # each line is considered as a seperate string
        for line in file:
            # ignore potential leading or trailing whitespaces and linebreaks
            first_digit, last_digit = find_digits(line.strip())
            two_digit_number = first_digit * 10 + last_digit
            total_sum += two_digit_number
    return total_sum


total = sum_of_numbers(file_name)
print(total)
