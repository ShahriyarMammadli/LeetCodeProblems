# Shahriyar Mammadli
# LeetCode problem '58. Length of Last Word' solution

def lengthOfLastWord(s):
    words = list(filter(lambda i: i != '', s.split(" ")))
    return 0 if s == "" or len(words) == 0 else len(words[-1])

print(lengthOfLastWord(" "))