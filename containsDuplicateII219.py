# Shahriyar Mammadli
# LeetCode problem '219. Contains Duplicate II' solution


def containsNearbyDuplicate(nums, k):
    index_dict = {}
    for index, value in enumerate(nums):
        if value in index_dict and index - index_dict[value] <= k:
            return True
        index_dict[value] = index
    return False

print(containsNearbyDuplicate([1, 2, 3, 1], 3))
