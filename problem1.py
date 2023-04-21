import math

# first solution
# lst = [i for i in range(2, 1000)]
#
# nums = []
#
# for i in lst:
#     if i % 3 == 0:
#         nums.append(i)
#         continue
#     if i % 5 == 0:
#         nums.append(i)
#         continue
#
# print(math.fsum(nums))

# second solution
print(math.fsum(i for i in range(2, 1000) if i % 3 == 0 or i % 5 == 0))
