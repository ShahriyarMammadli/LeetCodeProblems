# Shahriyar Mammadli
# LeetCode problem '1207. Unique Number of Occurrences' solution

def uniqueOccurrences(nums):
    # If an empty array passed, return True
    if len(nums) == 0:
        return True
    # Count positive and non-positive values separately
    dictPos= [0] * (max(nums) + 1)
    dictNeg = [0] * (abs(min(nums)) + 1)
    for i in nums:
        if i > 0:
            dictPos[i] = dictPos[i] + 1
        else:
            dictNeg[abs(i)] = dictNeg[abs(i)] + 1
    mergedDict = dictPos + dictNeg
    mergedDict.sort(reverse = True)
    # After sorting the dictionary of counts of each distinct value...
    # ...check if there is a duplicate
    for i in range(len(mergedDict)):
        if mergedDict[i] == 0:
            return True
        if mergedDict[i] == mergedDict[i-1]:
            return False

print(uniqueOccurrences([-1, -1, -1, -1,1,2, 2,3, 3,3]))