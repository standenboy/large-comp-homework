speed = 0
while speed < 10 or speed > 50:
    speed = int(input("speed: "))
wet = "null"
while wet != 'y' and wet != 'n':
    wet = input("is it wet: ").lower()
breakingdistance = speed / 5
if wet == 'y':
    breakingdistance = breakingdistance * 1.5
print(breakingdistance)
