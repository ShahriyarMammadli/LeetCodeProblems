# Shahriyar Mammadli
# LeetCode problem '349. Intersection of Two Arrays' solution


def interssection(nums1, nums2):
    # Use dictionary to check which values exists in both lists
    if len(nums1) == 0 or len(nums2) == 0:
        return []
    dict1 = [0] * (max(nums1) + 1)
    dict2 = [0] * (max(nums2) + 1)
    intersection = []
    for i in nums1:
        dict1[i] = 1
    for i in nums2:
        dict2[i] = 1
    for i in range(min(len(dict1), len(dict2))):
        if dict1[i] > 0 and dict2[i] > 0:
            intersection.append(i)
    return intersection

print(interssection([1,2, 4, 7,4, 4], [1,4,7]))