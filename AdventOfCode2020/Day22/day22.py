def get_winning_score(input):
    deck1, deck2 = [[int(c) for c in player.splitlines()[1:]] for player in input.split("\n\n")]
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1[0] > deck2[0]:
            deck1, deck2 = swap_cards(deck1, deck2)
        else:
            deck2, deck1 = swap_cards(deck2, deck1)
    winning_deck = deck1 if len(deck1) > 0 else deck2
    return sum(k * v for k, v in zip(winning_deck[::-1], range(1, len(winning_deck) + 1)))

def swap_cards(winning, losing):
    winning = winning[1:] + [winning[0], losing[0]]
    losing = losing[1:]
    return winning, losing

def test_input():
    test = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
    assert(get_winning_score(test)) == 306

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(get_winning_score(file.read()))