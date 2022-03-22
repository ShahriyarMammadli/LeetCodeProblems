# Shahriyar Mammadli
# LeetCode problem '521. Longest Uncommon Subsequence I' solution

def findLUSlength(a, b):
    return -1 if a == b else max(len(a), len(b))
