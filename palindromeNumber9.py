# Shahriyar Mammadli
# LeetCode problem '9. Palindrome Number' solution

def isPalindrome(X):
    if X < 0:
        return False
    if X == 0:
        return True
    stack = []
    while X != 0:
        stack.append(X % 10)
        X = int(X / 10)
    for i in range(int(len(stack)/2)):
        if stack[i] != stack[-1 - i]:
            return False
    return True
    # Slow but wiser alternative.
    # return True if stack[:int(len(stack)/2)] == stack[:int(len(stack)/2 - 0.5):-1] else False
print(isPalindrome(1221))
