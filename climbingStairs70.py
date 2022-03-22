# Shahriyar Mammadli
# LeetCode problem '70. Climbing Stairs' solution


def climbStairs(n):
    if n <= 2:
        return n
    # Initialize two variables to hold n-1 and n-2.
    n_2 = 1
    n_1 = 2
    current = -1
    for i in range(2, n):
        current = n_2 + n_1
        n_2 = n_1
        n_1 = current
    return current

print(climbStairs(4))