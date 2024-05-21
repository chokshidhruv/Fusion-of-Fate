import random
import time
from fractions import Fraction

def spinSpinner(): # for player 1
    print("Press Enter to spin the spinner...")
    input()
    print()
    spinner_outcomes = ["Multiplier", "Divisor"]
    spinner_result = random.choice(spinner_outcomes)
    print("Spinning the spinner...")
    time.sleep(2)
    print("The spinner for Player 1 landed on...", spinner_result)
    print()

    return spinner_result

def spinSpinnerAgain(): # for player 2
    print("Press Enter to spin the spinner...")
    input()
    print()
    spinner_outcomes = ["Multiplier", "Divisor"]
    spinner_result = random.choice(spinner_outcomes)
    print("Spinning the spinner...")
    time.sleep(2)
    print("The spinner for Player 2 landed on...", spinner_result)
    print()

    return spinner_result


def display_card(card, suit, operation):
    symbols_multiplier = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K"
    }
    symbols_divisor = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "A",
        12: "J",
        13: "Q",
        14: "K"
    }

    if operation == "Multiplier":
        symbol = symbols_multiplier[card]
    else:
        symbol = symbols_divisor[card]

    if suit == "Hearts":
        return symbol + " ♥"
    elif suit == "Diamonds":
        return symbol + " ♦"
    elif suit == "Clubs":
        return symbol + " ♣"
    elif suit == "Spades":
        return symbol + " ♠"

def draw_card(deck, operation):
    if operation == "Multiplier":
        card_values = list(range(1, 11)) + [11, 12, 13]
    else:
        card_values = list(range(2, 11)) + [11, 12, 13, 14]

    card = random.choice(card_values)
    while card not in deck:  # Check if the card is in the deck
        card = random.choice(card_values)

    deck.remove(card)
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    suit = random.choice(suits)
    print("Drawing a Card and Rolling a Dice...")
    time.sleep(2)  # Add a delay for dramatic effect
    return card, suit

def calculate_points(card, die_roll, operation):
    if operation == "Multiplier":
        if card in [1, 11, 12, 13]:
            points = Fraction(1, 1)
        else:
            points = Fraction(card, 1)
        points *= die_roll
    else:
        if card in [11, 12, 13, 14]:
            points = Fraction(12, 1)
        else:
            points = Fraction(card, 1)
        points /= die_roll
    
    return round(points)


def play_game():
    deck = list(range(1, 14)) * 4
    random.shuffle(deck)
    player1_points = 0
    player2_points = 0

    print("Welcome to Fusion of Fate: Ultimate Card, Spinner, and Dice probability game!")
    print()

    spinner_result_p1 = spinSpinner()
    spinner_result_p2 = spinSpinnerAgain()

    for turn in range(1, 8):
        print(f"--- Turn {turn} ---")
        input("Press Enter for Player 1 to draw a card & roll dice.")
        print()

        # Player 1's turn
        card, suit = draw_card(deck, spinner_result_p1)
        print("Player 1 draws card:", display_card(card, suit, spinner_result_p1))
        die_roll = random.randint(1, 6)
        print("Player 1 rolls the die:", die_roll)

        player1_turn_points = calculate_points(card, die_roll, spinner_result_p1)
        print("Player 1 points for this turn:", player1_turn_points)
        print()
        player1_points += player1_turn_points

        input("Press Enter for Player 2 to draw a card & roll dice.")
        print()

        # Player 2's turn
        card, suit = draw_card(deck, spinner_result_p2)
        print("Player 2 draws card:", display_card(card, suit, spinner_result_p2))
        die_roll = random.randint(1, 6)
        print("Player 2 rolls the die:", die_roll)

        player2_turn_points = calculate_points(card, die_roll, spinner_result_p2)
        print("Player 2 points for this turn:", player2_turn_points)
        print()
        player2_points += player2_turn_points

    # Determine the winner
    print("Game Over...")
    print("Player 1 total points:", player1_points)
    print("Player 2 total points:", player2_points)
    print()

    if player1_points == player2_points:
        print("It's a tie!")
    elif player1_points > player2_points:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

play_game()
