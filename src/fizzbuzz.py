import sys

for i in range(1,101):
    sys.stdout.write("\n")
    sys.stdout.write(f"{i} ")
    if i % 3 == 0:
        sys.stdout.write("fizz")
    if i % 5 == 0:
        sys.stdout.write("buzz")

sys.stdout.write("\n")
