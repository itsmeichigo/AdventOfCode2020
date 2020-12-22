from collections import deque

def get_winning_score(input, recursive):
    player1, player2 = tuple(deque([int(c) for c in player.splitlines()[1:]]) for player in input.split("\n\n"))
    return play_recursive_combat(player1, player2)[0] if recursive else play_combat(player1, player2)

def calculate_score(deck):
    return sum(k * v for k, v in zip(list(deck)[::-1], range(1, len(deck) + 1)))

def play_combat(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2: deck1.extend([card1, card2])
        else: deck2.extend([card2, card1])
    return max(calculate_score(deck1), calculate_score(deck2))

def play_recursive_combat(deck1, deck2):
    rounds = set()
    while len(deck1) > 0 and len(deck2) > 0:
        score1, score2 = calculate_score(deck1), calculate_score(deck2)
        if (score1, score2) in rounds:
            return score1, 1
        rounds.add((score1, score2))
        card1, card2 = deck1.popleft(), deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            score, winner = play_recursive_combat(deque(list(deck1)[:card1]), deque(list(deck2)[:card2]))
            if winner == 1: deck1.extend([card1, card2])
            else: deck2.extend([card2, card1])
        else: 
            if card1 > card2: deck1.extend([card1, card2])
            else: deck2.extend([card2, card1])
    winner = 1 if len(deck1) > 0 else 2
    return max(calculate_score(deck1), calculate_score(deck2)), winner

def test_input():
    with open("test.txt") as file:
        test = file.read()
        assert(get_winning_score(test, False)) == 306
        assert(get_winning_score(test, True)) == 291

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        input = file.read()
        print(get_winning_score(input, False))
        print(get_winning_score(input, True))