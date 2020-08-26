# Shahriyar Mammadli
# LeetCode problem '189. Rotate Array' solution

def rotate(nums, k):
    nums[:] = [] if len(nums) == 0 else nums[len(nums) - k%len(nums):] + nums[:len(nums)-k%len(nums)]
    return nums

print(rotate([1,2,3,4,5,6,7], 3))
