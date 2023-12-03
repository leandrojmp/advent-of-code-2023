from sys import argv

MAX_GREEN = 13
MAX_BLUE = 14
MAX_RED = 12

def validate_game(line):
    game_number = line.split(":")[0].split(" ")[1]
    game_sets = line.split(":")[1].replace("\n","").split(";")
    game_sets = [s.split(",") for s in game_sets]
    invalid = 0
    set_data = {
        "red": [0],
        "green": [0],
        "blue": [0],
        "valid": True,
        "game_number": int(game_number)
    }
    for set in game_sets:
        for cube in set:
            match cube.strip().split(" ")[1]:
                case "red":
                    set_data['red'].append(int(cube.strip().split(" ")[0]))
                    if int(cube.strip().split(" ")[0]) > MAX_RED:
                        invalid = invalid + 1
                case "green":
                    set_data['green'].append(int(cube.strip().split(" ")[0]))
                    if int(cube.strip().split(" ")[0]) > MAX_GREEN:
                        invalid = invalid + 1
                case "blue":
                    set_data['blue'].append(int(cube.strip().split(" ")[0]))
                    if int(cube.strip().split(" ")[0]) > MAX_BLUE:
                        invalid = invalid + 1
    set_data['red'] = max(set_data['red'])
    set_data['green'] = max(set_data['green'])
    set_data['blue'] = max(set_data['blue'])
    if invalid > 0:
        set_data['valid'] = False
    return set_data

def min_cubes(set_data):
    del set_data['valid']
    del set_data['game_number']
    for key in set_data:
        if int(set_data[key]) == 0:
            set_data[key] = 1
    cube_power = set_data['red'] * set_data['green'] * set_data['blue']
    return int(cube_power)


with open(argv[1],'r') as input_file:
    valid_games = 0
    sum_power = 0
    for line in input_file:
        current_set = validate_game(line)
        if current_set['valid']:
            valid_games = valid_games + current_set['game_number']
        sum_power = sum_power + min_cubes(validate_game(line))
    print("valid games: {}".format(valid_games))
    print("sum of power sets: {}".format(sum_power))
