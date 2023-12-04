scratchcard_file = "input.txt"
card_dict = {}  # contains card id and two number sets
matching_elements = {}  # contains card id and one set with elements that are in both number sets


def read_scratchcards_from_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            card_id, number_sets = parse_file_line(line)
            card_dict[card_id] = number_sets

    return card_dict


def parse_file_line(line):
    game_id, numbers = line.split(":")
    numbers = numbers.split("|")
    number_sets = []  # contains two sets of numbers, the first is the winning numbers, the second my numbers

    for number in numbers:
        number_set = []
        elements = number.split()
        for item in elements:
            number_set.append(item)
        number_sets.append(number_set)
    return int(game_id.split()[1]), number_sets


def my_number_is_winning_number():

    for key, value in card_dict.items():
        winning_numbers, my_numbers = value
        matches = [element for element in my_numbers if element in winning_numbers]
        matching_elements[key] = matches

    return matching_elements


def calculate_worth_of_pile():
    element_counts = {}
    sum_of_card_worth = 0
    for key, matches in matching_elements.items():
        count = len(matches)
        if count > 0:
            sum_of_card_worth += 2**(count - 1)
        else:
            sum_of_card_worth += 0
        element_counts[key] = count

    print(sum_of_card_worth)


read_scratchcards_from_file(scratchcard_file)
my_number_is_winning_number()
calculate_worth_of_pile()