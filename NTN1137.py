# Shahriyar Mammadli
# LeetCode problem '1137. N-th Tribonacci Number' solution

def tribonacci(n):
    result = 0
    prev1 = 0
    prev2 = 1
    prev3 = 1
    if n < 2:
        return n
    if n == 2:
        return 1
    for i in range(3, n+1):
        result = prev1 + prev2 + prev3
        prev1 = prev2
        prev2 = prev3
        prev3 = result
    return result % 2147483647

# Recursive solution
# def tribonacci(n):
#     if n < 2:
#         return n
#     if n == 2:
#         return 1
#     return (tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)) % 2147483647

print(tribonacci(25))