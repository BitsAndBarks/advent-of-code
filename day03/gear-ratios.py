engine_file = "input.txt"

# template for the cells to check around the current one. format: (tr, tc) <- template row, template column
SURROUNDING_CELLS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


# returns input as a list of lists (a 2D array)
def read_schematic(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]


# helper function to avoid index out of range error when checking adjacent cells
def is_cell_in_range(schematic, row, col):
    return 0 <= row < len(schematic) and 0 <= col < len(schematic[0])


# Function for part 1. Extracts all numbers and then checks if a symbol is adjacent. If yes, store number.
def extract_adjacent_numbers(schematic):
    adjacent_numbers = []

    for row in range(len(schematic)):
        col = 0
        while col < len(schematic[row]):
            if schematic[row][col].isdigit():
                number_start = col
                # extract the whole number (can consist of multiple digits)
                while col < len(schematic[row]) and schematic[row][col].isdigit():
                    col += 1
                number = ''.join(schematic[row][number_start:col])

                # check for adjacent symbols for each digit in the number
                is_digit_adjacent_to_symbol = False
                for i in range(number_start, col):
                    for tr, tc in SURROUNDING_CELLS:
                        # add offset to the surrounding cell template and calculates actual row and actual column
                        ar, ac = row + tr, i + tc
                        # loop through the whole number and check if any is adjacent to a symbol
                        if (is_cell_in_range(schematic, ar, ac)
                                and not schematic[ar][ac].isdigit()
                                and schematic[ar][ac] != '.'):
                            is_digit_adjacent_to_symbol = True
                            break
                    # leave loop once a digit in a number is adjacent to a symbol
                    if is_digit_adjacent_to_symbol:
                        break

                if is_digit_adjacent_to_symbol:
                    adjacent_numbers.append(number)
            else:
                col += 1

    return adjacent_numbers


# Function for part 2. Loop through schematic and add numbers if they're adjacent to a *.
# Then check if there are exactly 2 numbers adjacent to the same '*'. If yes, store them in a pairs array.
def find_pairs_adjacent_to_star(schematic):
    pairs = []

    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col] == "*":
                adjacent_numbers = {}

                for tr, tc in SURROUNDING_CELLS:
                    ar, ac = row + tr, col + tc
                    if is_cell_in_range(schematic, ar, ac) and schematic[ar][ac].isdigit():
                        number, position = extract_number(schematic, ar, ac)
                        adjacent_numbers[position] = number

                if len(adjacent_numbers) == 2:
                    pairs.append(tuple(adjacent_numbers.values()))

    return pairs


# Number extraction function for part 2. digit adjacent to symbol may not be starting digit of a number.
# Checks left side of digit if there are more digits. Then moves right to extract rest of number.
def extract_number(schematic, row, col):
    # find the start of the number by moving left
    while col > 0 and schematic[row][col - 1].isdigit():
        col -= 1
    number = ''
    # Extract the entire number
    while col < len(schematic[row]) and schematic[row][col].isdigit():
        number += schematic[row][col]
        col += 1
    return number, (row, col)


def main():
    engine_schematic = read_schematic(engine_file)

    print("Part 1:")
    numbers_adjacent_to_symbols = extract_adjacent_numbers(engine_schematic)
    sum_of_numbers = sum(int(number) for number in numbers_adjacent_to_symbols)
    print("All numbers that are adjacent to a symbol:", numbers_adjacent_to_symbols)
    print("Sum of values:", sum_of_numbers)

    print("Part 2:")
    number_pairs = find_pairs_adjacent_to_star(engine_schematic)
    sum_of_pair_products = sum(int(a) * int(b) for a, b in number_pairs)
    print("Pairs adjacent to *:", number_pairs)
    print("Sum of products:", sum_of_pair_products)


if __name__ == "__main__":
    main()
