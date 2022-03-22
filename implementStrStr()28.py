# Shahriyar Mammadli
# LeetCode problem '28. Implement strStr()' solution

def strStr(haystack, needle):
    if needle == "":
        return 0
    for index in range(len(haystack)-len(needle) + 1):
        if haystack[index:index + len(needle)] == needle:
            return index
    return -1

print(strStr("hello", "lo"))