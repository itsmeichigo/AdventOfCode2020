def encrypt(subject, loopsize):
    current = 1
    for _ in range(loopsize):
        current *= subject
        current %= 20201227
    return current

def decrypt(subject, public_key):
    current, loopzize = public_key, 0
    while current != 1:
        divider, x = 0, current
        while x % 7:
            x = 20201227 * divider + current
            divider += 1
        current = int(x / 7)
        loopzize += 1
    return loopzize
    

assert(encrypt(7, 8)) == 5764801
assert(encrypt(7, 11)) == 17807724

assert(decrypt(7, 5764801)) == 8
assert(decrypt(7, 17807724)) == 11

assert(encrypt(17807724, 8)) == 14897079
assert(encrypt(5764801, 11)) == 14897079

with open("data.txt") as file:
    input = file.read()
    card_pk, door_pk = [int(i) for i in input.splitlines()]
    card_loopsize = decrypt(7, card_pk)
    encryption_key = encrypt(door_pk, card_loopsize)
    print(card_loopsize, encryption_key)