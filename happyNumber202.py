# Shahriyar Mammadli
# LeetCode problem '202. Happy Number' solution


def isHappy(n):
    hash_table = set()
    while n != 1:
        if n in hash_table:
            return False
        hash_table.add(n)
        n = list(str(n))
        n = list(map(int, n))
        n = sum(list(map(lambda x: x ** 2, n)))
    return True


print(isHappy(19))


