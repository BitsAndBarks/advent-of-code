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


# Checks all elements in second array if they also appear in first array. If yes, they're a winning number.
def is_my_number_winning_number():
    for key, value in card_dict.items():
        winning_numbers, my_numbers = value
        matches = [element for element in my_numbers if element in winning_numbers]
        matching_elements[key] = matches

    return matching_elements


# part 1
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

    return sum_of_card_worth


# part 2
def calculate_total_scratchcards():
    total_cards = {key: 1 for key in card_dict}  # Start with 1 instance of each card
    cards_to_process = total_cards.copy()  # Cards to process in the current iteration

    while cards_to_process:
        new_cards = {key: 0 for key in card_dict}  # Temporary storage for newly won cards

        for key, count in cards_to_process.items():
            if key not in matching_elements or not matching_elements[key]:  # Skip if no matches
                continue

            match_count = len(matching_elements[key])

            for i in range(1, match_count + 1):
                next_card = key + i
                if next_card in total_cards:
                    new_cards[next_card] += count  # Win new cards based on the count of the current card

        # Update total_cards with the new cards won
        for key, count in new_cards.items():
            total_cards[key] += count

        # Set up cards for the next iteration
        cards_to_process = {k: v for k, v in new_cards.items() if v > 0}

    return sum(total_cards.values())


def main():
    read_scratchcards_from_file(scratchcard_file)
    is_my_number_winning_number()

    # part 1
    pile_worth = calculate_worth_of_pile()
    print("Scratchcards are worth in total: ", pile_worth)

    # part 2
    total_scratchcards = calculate_total_scratchcards()
    print("Total amount of received scratchcards:", total_scratchcards)


if __name__ == "__main__":
    main()
