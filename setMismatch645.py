# Shahriyar Mammadli
# LeetCode problem '645. Set Mismatch' solution
from functools import reduce
def findErrorNums(nums):
    return [sum(nums) - sum(set(nums)), (set(nums) ^ set(range(1, len(nums) + 1))).pop()]


print(findErrorNums([2,2]))
