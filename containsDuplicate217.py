# Shahriyar Mammadli
# LeetCode problem '217. Contains Duplicate' solution

def containsDuplicate(nums):
    return len(list(set(nums))) != len(nums)

print(containsDuplicate([1, 2, 3, 3]))