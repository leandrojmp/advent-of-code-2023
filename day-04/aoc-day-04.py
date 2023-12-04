from sys import argv
import re

def calculate_winning_numbers(line):
    card_number = line.split(":")[0]
    card_winning_numbers = line.split(":")[1].split("|")[0].strip(" ").split(" ")
    card_winning_numbers = list(filter(None, card_winning_numbers))
    card_my_numbers = line.split(":")[1].split("|")[1].strip(" ").replace("\n","").split(" ")
    card_my_numbers = list(filter(None, card_my_numbers))
    winning_numbers = set(card_winning_numbers) & set(card_my_numbers)
    card_wins = {
        "Card": card_number,
        "Winnings": winning_numbers
    }
    return card_wins

def calculate_copies(cards, wins):
    re.findall(r'\d+', line)
    card_and_wins = "{}:{}".format(
        re.findall(r'\d+', wins['Card'])[0],
        len(wins['Winnings']))
    cards.append(card_and_wins)

def calculate_cards(cards, wins, lines):
    for r in range(len(lines)):
        for w in range(1,int(wins[r].split(":")[1])+1):
            if r+w < len(lines):
                cards[r+w] += cards[r]
    return sum(cards)

with open(argv[1],'r') as input_file:
    lines = input_file.read().splitlines()
    total_points = 0
    cards = [1] * len(lines)
    win_list = []
    for line in lines:
        wins = calculate_winning_numbers(line)
        calculate_copies(win_list, wins)
        if len(wins['Winnings']) > 0:
            calculate_points = len(wins['Winnings']) - 1
            total_points = total_points + (2**calculate_points)
    total_cards = calculate_cards(cards, win_list, lines)
    print("winnings: {}".format(total_points))
    print("cards: {}".format(total_cards))
