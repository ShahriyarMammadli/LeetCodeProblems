# Shahriyar Mammadli
# LeetCode problem '35. Search Insert Position' solution

def searchInsert(nums, target):
    start_index = 0
    end_index = len(nums)
    while end_index > start_index:
        middle_index = int((start_index + end_index) / 2)
        if start_index + 1 == end_index:
            return start_index if target <= nums[middle_index] else end_index
        if nums[middle_index] > target:
            end_index = middle_index
        elif nums[middle_index] < target:
            start_index = middle_index
        elif nums[middle_index] == target:
            return middle_index

print(searchInsert([1,], 0))

