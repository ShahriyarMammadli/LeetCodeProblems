# Shahriyar Mammadli
# LeetCode problem '509. Fibonacci Number' solution

def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib(N-1) + fib(N-2)

print(fib(2))
