import math

lst = [i for i in range(2, 1000)]

nums = []

for i in lst:
    if i % 3 == 0:
        nums.append(i)
        continue
    if i % 5 == 0:
        nums.append(i)
        continue

print(math.fsum(nums))