# Shahriyar Mammadli
# LeetCode problem '1. Two Sum' solution

def twoSum(nums, target):
    # In each iteration check if in the reamining part of the array...
    # ...(means values after current index)...
    # ...there is a value that be summed...
    # ...to the target with the value of current index...
    # ...i.e. check if there occurs a value that satisfies nums[i] + value = target
    for i in range(len(nums)):
        if target - nums[i] in nums[(i + 1):]:
            return i, nums[(i + 1):].index(target - nums[i]) + i + 1
    return None

print(twoSum([2, 7, 11, 15], 9))