# Shahriyar Mammadli
# LeetCode problem '136. Single Number' solution

def singleNumber(nums):
    record = set()
    for i in nums:
        if i not in record:
            record.add(i)
        else:
            record.remove(i)
    return record.pop()

print(singleNumber([2, 2, 1]))

print(1 ^ 2)


