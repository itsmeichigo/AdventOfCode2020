def get_winning_score(player1, player2, recursive):
    return play_recursive_combat(player1, player2)[0] if recursive else play_combat(player1, player2)

def calculate_score(deck):
    return sum(k * v for k, v in zip(deck[::-1], range(1, len(deck) + 1)))

def play_combat(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1[0] > deck2[0]: deck1, deck2 = swap_cards(deck1, deck2)
        else: deck2, deck1 = swap_cards(deck2, deck1)
    return max(calculate_score(deck1), calculate_score(deck2))

def play_recursive_combat(deck1, deck2):
    rounds = set()
    while len(deck1) > 0 and len(deck2) > 0:
        score1, score2 = calculate_score(deck1), calculate_score(deck2)
        if (score1, score2) in rounds:
            return score1, 1
        rounds.add((score1, score2))
        card1, card2 = deck1[0], deck2[0]
        if len(deck1[1:]) >= card1 and len(deck2[1:]) >= card2:
            score, winner = play_recursive_combat(deck1[1:card1+1], deck2[1:card2+1])
            if winner == 1: deck1, deck2 = swap_cards(deck1, deck2)
            else: deck2, deck1 = swap_cards(deck2, deck1)
        else: 
            if deck1[0] > deck2[0]: deck1, deck2 = swap_cards(deck1, deck2)
            else: deck2, deck1 = swap_cards(deck2, deck1)
    winner = 1 if len(deck1) > 0 else 2
    return max(calculate_score(deck1), calculate_score(deck2)), winner
    
def swap_cards(winning, losing):
    winning = winning[1:] + [winning[0], losing[0]]
    losing = losing[1:]
    return winning, losing

def test_input():
    with open("test.txt") as file:
        player1, player2 = [[int(c) for c in player.splitlines()[1:]] for player in file.read().split("\n\n")]
        assert(get_winning_score(player1, player2, False)) == 306
        assert(get_winning_score(player1, player2, True)) == 291

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        player1, player2 = [[int(c) for c in player.splitlines()[1:]] for player in file.read().split("\n\n")]
        print(get_winning_score(player1, player2, False))
        print(get_winning_score(player1, player2, True))