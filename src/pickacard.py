import random

cards = []
for i in range(1, 100):
    cards[i-1] = random.randint(1, 100)

cardpos = -1

while True:
    while cardpos < 1 or cardpos > 100:
        cardpos = int(input("position of card to swap: "))
    cards[cardpos] = random.randint(1, 100)
    
    sequential = 0
    
    for i in range(len(cards)):
        if cards[i] == cards[i+1] + 1:
            sequential = sequential + 1
        else:
            sequential = 0
        if sequential == 5:
            break

print("the player won the game")

    

