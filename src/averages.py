numofnums = int(input("how many nums are you going to use: "))
nums = []
for i in range(numofnums):
    nums.append(int(input(f"number {i}: ")))

print(sum(nums)/numofnums)
