import random

YOU = 0
COMP = 1

CHOICES = ['r', 'p', 's']
CHOICE_MAP = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}


def play_game(best_of=3):
    """
    Play a game of rock, paper, scissors
    """
    score = [0, 0]

    print(f'Rock, paper, scissors - best of {best_of}')

    while True:
        winner = run_round()
        update_score(score, winner)
        game_winner = game_over(best_of, score)

        if game_winner is not None:
            break

    won_or_lost = 'won' if game_winner == YOU else 'lost'
    print(f"You {won_or_lost} {score[YOU]} games to {score[COMP]}")


def update_score(score, winner):
    if winner is not None:
        score[winner] += 1
    print(f'{score[YOU]} - {score[COMP]}')


def run_round():
    your_choice = get_user_choice()
    computer_choice = random.choice(CHOICES)

    winner = determine_winner(your_choice, computer_choice)
    print_outcome(winner, your_choice, computer_choice)
    return winner


def determine_winner(choice, computer_choice):
    """
    Returns:
        YOU if you won
        COMP if computer won
        None if it was a tie
    """
    if choice == 'r':
        return YOU if computer_choice == 's' else COMP
    elif choice == 'p':
        return YOU if computer_choice == 'r' else COMP
    elif choice == 's':
        return YOU if computer_choice == 'p' else COMP
    else:
        return None


def print_outcome(winner, you, computer):
    if winner == YOU:
        result = 'WINS against'
    elif winner == COMP:
        result = 'LOSES to'
    else:
        result = "TIES with"
    print(f'{CHOICE_MAP[you]} {result} {CHOICE_MAP[computer]}')


def game_over(best_of, score):
    num_wins_needed = best_of / 2
    if score[YOU] == num_wins_needed:
        return YOU
    elif score[COMP] == num_wins_needed:
        return COMP
    return None


def get_user_choice():
    return input("\nRock (r), paper (p), or scissors (s)?: ").lower().strip()


if __name__ == '__main__':
    play_game()
