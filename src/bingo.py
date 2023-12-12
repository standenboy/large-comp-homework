import random

possible = ["cpu", "alu", "ram", "binary", "lan", "wan", "pixel", "printer", "repo"]
ans = ["the processor", "the bit that does logic", "the bit that stores stuff", "a counting system", "a local network", "a wide network", "a led on a display", "makes fancy paper", "a folder that stores a code base"]

board = [
        [1,1,1],
        [1,1,1],
        [1,1,1],
         ]

for i in range(3):
    for j in range(3):
        board[i][j] = possible[random.randint(0, 8)]

for i in ans:
    print(i)
    anwser = input("what is this: ")
    if possible.index(anwser) == ans.index(i):
        print("you got it")



