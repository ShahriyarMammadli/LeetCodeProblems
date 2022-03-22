# Shahriyar Mammadli
# LeetCode problem '53. Maximum Subarray' solution

def maxSubArray(nums):
    current, answer = 0, 0
    for value in nums:
        current = max(current + value, 0)
        answer = max(current, answer)
    return answer or max(nums)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
