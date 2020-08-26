# Shahriyar Mammadli
# LeetCode problem '26. Remove Duplicates from Sorted Array' solution

def removeDup(nums):
    # If empty array
    if (len(nums) < 1):
        return len(nums)
    size = len(nums)
    i = 1
    while i < size:
        if nums[i] == nums[i - 1]:
            nums[:] = nums[:i] + nums[i + 1:]
            size = size - 1
            i = i - 1
        i = i + 1
    if len(nums) > 1 and nums[-1] == nums[-2]:
        nums[:] = nums[:-1]
    return len(nums)

print(removeDup([]))
