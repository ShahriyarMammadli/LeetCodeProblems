# Shahriyar Mammadli
# LeetCode problem '674. Longest Continuous Increasing Subsequence' solution

def findLengthOfLCIS(nums):
    # Using dictionary logic firstly new array created. This...
    # ...array includes difference  of value in current index and value...
    # ...in previous index. Thus we can know that whether array kept increasing if...
    # ...value in the new array is positive newArr[i] = oldArr[i] - oldArr[i-1]
    if len(nums) == 0:
        return 0
    temp = [0] * (len(nums) - 1)
    for i in range(1, len(nums)):
        temp[i - 1] = nums[i] - nums[i - 1]
    count = 0
    maxArr = []
    tempArr = []
    countMax = 0
    # Using the dictionary, longest increasing sub array is found
    for i in range(0, len(temp)):
        if (temp[i] > 0):
            tempArr.append(i + 1)
        elif (temp[i] <= 0):
            if (len(tempArr) > len(maxArr)):
                maxArr = tempArr
                tempArr = []
            else:
                tempArr = []
    if (len(tempArr) > len(maxArr)):
        maxArr = tempArr
        tempArr = []
    return len(maxArr) + 1

print(findLengthOfLCIS([1,3,5,4,7]))
