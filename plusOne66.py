# Shahriyar Mammadli
# LeetCode problem '66. Plus One' solution

def plusOne(digits):
    if digits[-1] == 9:
        if len(digits) == 1:
            digits[0] = 0
        for index, value in enumerate(digits[::-1]):
            if value == 9:
                digits[len(digits)-index - 1] = 0
                digits[len(digits) - index - 2] += 1
            else:
                break
    else:
        digits[-1] += 1
    # special case occurs in case of overflow
    if digits[0] == 0:
        digits = [0] * len(digits)
        digits.insert(0, 1)
    return digits

print(plusOne([9]))