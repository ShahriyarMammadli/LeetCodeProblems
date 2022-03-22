# Shahriyar Mammadli
# LeetCode problem '258. Add Digits' solution

def addDigits(num):
    if num < 10:
        return num
    result = 0
    while True:
        result += num % 10
        num //= 10
        if num == 0 and result < 10:
            break;
        if num == 0:
            num = result
            result = 0
    return result


print(addDigits(38))
