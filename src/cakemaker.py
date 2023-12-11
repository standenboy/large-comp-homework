while True:
    eggs = int(input("how many eggs are there: "))
    if eggs > 0 and eggs < 8:
        break
print(f"you need {100 * eggs}g of flour and {50 * eggs}g of butter")
