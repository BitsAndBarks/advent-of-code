file_name = "input.txt"

NUMERAL_TO_DIGIT = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}


def find_digits_and_numerals(s):
    digits = []
    i = 0
    while i < len(s):
        matched = False
        # append digits where they appear in the string
        if s[i].isdigit():
            digits.append(s[i])
            i += 1
            continue
        for numeral, digit in NUMERAL_TO_DIGIT.items():
            if s[i:i + len(numeral)].lower() == numeral:
                digits.append(digit)
                # go back one step in case two numerals overlap, e.g. sevenine
                i += len(numeral) - 1
                matched = True
                break
        if not matched:
            i += 1

    # if string does not return any values, add 0 to avoid IndexError
    if not digits:
        return [0, 0]
    # if string only contains one digit, use it for both first and last
    elif len(digits) == 1:
        return [int(digits[0]), int(digits[0])]
    else:
        return [int(digits[0]), int(digits[-1])]


def sum_of_numbers(input_file):
    total_sum = 0
    with open(input_file, 'r') as file:
        # each line is considered as a separate string
        for line in file:
            # ignore potential leading or trailing whitespaces and linebreaks
            first_digit, last_digit = find_digits_and_numerals(line.strip())
            two_digit_number = first_digit * 10 + last_digit
            total_sum += two_digit_number
    return total_sum


def main():
    total = sum_of_numbers(file_name)
    print('Total:', total)


if __name__ == "__main__":
    main()
