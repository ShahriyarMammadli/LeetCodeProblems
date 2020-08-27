# Shahriyar Mammadli
# LeetCode problem '724. Find Pivot Index' solution

def pivotIndex(nums):
    sumAll = sum(nums)
    for i in range(len(nums)):
        sumAll = sumAll - nums[i]
        if sumAll == (sum(nums) - nums[i]) / 2:
            return i
    return -1

print(pivotIndex([]))