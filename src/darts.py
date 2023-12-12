def getdartstotal():
    darts = [100,100,100]
    for i in range(3):
        while darts[i] > 60:
            darts[i] = int(input(f"what is the value of dart {i}: "))
    return sum(darts)

print(f"you are {180 - getdartstotal()} away from a perfect score")
