# Shahriyar Mammadli
# LeetCode problem '263. Ugly Number' solution

def isUgly(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n //= 3
        elif n % 5 == 0:
            n //= 5
        else:
            return False
    return True

print(isUgly(0))
