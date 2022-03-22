# Shahriyar Mammadli
# LeetCode problem '169. Majority Element' solution

# Boyer–Moore majority vote algorithm
def majorityElement(nums):
    majority = 0
    count = 0
    for val in nums:
        if count == 0:
            majority = val
        if majority == val:
            count += 1
        else:
            count -= 1
    return majority


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
