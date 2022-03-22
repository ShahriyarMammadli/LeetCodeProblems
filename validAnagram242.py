# Shahriyar Mammadli
# LeetCode problem '53. Maximum Subarray' solution

def isAnagram(s, t):
    # if len(s) != len(t):
    #     return False
    # stack = []
    # for letter in s:
    #     stack.append(letter)
    # for letter in t:
    #     if letter in stack:
    #         stack.remove(letter)
    # return len(stack) == 0
    letter_dict = [0] * 26
    if len(s) != len(t):
        return False
    for index in range(len(s)):
        letter_dict[ord(s[index]) - 97] += 1
        letter_dict[ord(t[index]) - 97] -= 1
    return all(x == 0 for x in letter_dict)

print(isAnagram("rat", "tar"))
