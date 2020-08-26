# Shahriyar Mammadli
# LeetCode problem '27. Remove Element' solution

def removeElement(nums, val):
    length = len(nums)
    index = 0
    while index < length:
        if nums[index] == val:
            del nums[index]
            length = length - 1
            index = index - 1
        index = index + 1
    return len(nums)

print(removeElement([0,1,2,2,3,0,4,2], 2))