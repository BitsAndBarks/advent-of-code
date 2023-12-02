game_file = 'input.txt'

MAX_BALLS = {'red': 12, 'green': 13, 'blue': 14}
games_dict = {}  # contains all games with their results {g_id: [(res_r1},{res_r2},{res_r3}], d_id: ...}


# reads results of all games from a text file and returns a dictionary of games
def read_games_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            game_id, round_results = parse_game_line(line)
            games_dict[game_id] = round_results
    return games_dict


# lines from text file need parsing, will then be stored in dictionary
def parse_game_line(line):
    game_id, rounds = line.split(':')
    rounds = rounds.strip().split(';')
    round_results = []  # contains results of each round of a game [(res_r1},{res_r2},{res_r3}]

    for round_result in rounds:
        round_dict = {}
        elements = round_result.strip().split(', ')
        for item in elements:
            count, colour = item.split()
            round_dict[colour] = int(count)
        round_results.append(round_dict)
    return int(game_id.split()[1]), round_results


# checks if a round in a game is possible
def is_round_possible(round_results):
    for color, count in round_results.items():
        if count > MAX_BALLS[color]:
            return False
    return True


# checks if a game is possible (when all rounds are possible)
def is_game_possible(round_results):
    for round_result in round_results:
        if not is_round_possible(round_result):
            return False
    return True


# adds up all id's of possible games
def sum_of_possible_games_ids(games):
    possible = []
    for game_id, game_results in games.items():
        if is_game_possible(game_results):
            possible.append(game_id)
    return sum(possible)


# calculates minimum amount of required balls per game, includes all games
def min_balls_per_game(game_results):
    min_balls = {'red': 0, 'green': 0, 'blue': 0}
    for round_result in game_results:
        for color in min_balls.keys():
            min_balls[color] = max(min_balls[color], round_result.get(color, 0))
    return min_balls


# calculates power of each minimum set and sums up the results
def product_of_minimum_balls(games):
    total_product_sum = 0
    for game_results in games.values():
        min_balls = min_balls_per_game(game_results)
        product = min_balls['red'] * min_balls['green'] * min_balls['blue']
        total_product_sum += product
    return total_product_sum


def main():
    games = read_games_from_file(game_file)

    # part 1
    sum_of_ids = sum_of_possible_games_ids(games)
    print('Sum of id\'s:', sum_of_ids)

    # part 2
    total_product_sum = product_of_minimum_balls(games)
    print('Sum of powers:', total_product_sum)


if __name__ == "__main__":
    main()
