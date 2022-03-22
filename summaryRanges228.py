# Shahriyar Mammadli
# LeetCode problem '228. Summary Ranges' solution

def summaryRanges(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [str(nums[0])]
    start_val = end_val = nums[0]
    result = []
    for index in range(1, len(nums)):
        if nums[index] != nums[index-1] + 1:
            result.append(str(start_val) + "->" + str(end_val) if start_val != end_val else str(start_val))
            start_val = end_val = nums[index]
        else:
            end_val = nums[index]
    result.append(str(start_val) + "->" + str(end_val) if start_val != end_val else str(start_val))
    return result


print(summaryRanges([0, 2, 3]))