weekend = "null"
while weekend.lower() != 'y' and weekend.lower() != 'n':
    weekend = input("is it a weekend (y/n): ")
while True:
    temp = int(input("whats the temp: "))
    if temp < 45 and temp > 20:
        break

if temp > 38:
    sold = 120
elif temp >= 31 and temp <= 38:
    sold = 150
else:
    sold = 100

if weekend == 'y':
    sold = sold * 2

print(f"you sold {sold} icecream")
