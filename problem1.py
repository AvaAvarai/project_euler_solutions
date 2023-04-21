"""
Problem #1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# This solution makes use of the Sieve of Eratosthenes.

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
# This solution uses the same algorithm in a single loop.
print(math.fsum(i for i in range(2, 1000) if i % 3 == 0 or i % 5 == 0))
