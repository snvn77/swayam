import string
import random

l = list(string.ascii_letters)
card_1 = [None]*5
card_2 = [None]*5

pos_1 = random.randint(0,4)
pos_2 = random.randint(0,4)

common = random.choice(l)
l.remove(common)

for i in range(5):
    if pos_1==pos_2 and i==pos_1:
        card_1[i] = common
        card_2[i] = common
    elif pos_1!=pos_2 and i==pos_1:
        card_1[i] = common
        card_2[i] = random.choice(l)
        l.remove(card_2[i])
    elif pos_1!=pos_2 and i==pos_2:
        card_2[i] = common
        card_1[i] = random.choice(l)
        l.remove(card_1[i])
    else:
        card_1[i] = random.choice(l)
        l.remove(card_1[i])
        card_2[i] = random.choice(l)
        l.remove(card_2[i])

print(f"The cards are {card_1} and {card_2}")
guess = input('Spot the common symbol!! Enter your guess: ').strip()
if len(guess) == 1 and guess in string.ascii_letters:
    if guess == common:
        print("RIGHT!!")
    else:
        print("WRONG!!")
        print(f"The common symbol was: {common}")
else:
    print("The input must be a single alphabet")