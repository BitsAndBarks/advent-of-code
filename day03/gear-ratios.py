engine_file = 'input.txt'

# template for the cells to check around the current one. format: (tr, tc) <- template row, template column
SURROUNDING_CELLS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


# returns input as a list of lists (a 2D array)
def read_schematic(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]


# helper function to avoid index out of range error when checking adjacent cells
def is_cell_in_range(schematic, row, col):
    return 0 <= row < len(schematic) and 0 <= col < len(schematic[0])


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


def main():
    engine_schematic = read_schematic(engine_file)

    result = extract_adjacent_numbers(engine_schematic)
    sum_of_values1 = sum(int(number) for number in result)
    print("Permanent Storage (Adjacent Numbers):", result)
    print("Sum of Values:", sum_of_values1)
