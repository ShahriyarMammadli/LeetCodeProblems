# Shahriyar Mammadli
# LeetCode problem '38. Count and Say' solution

def helper(oldStr, n):
    if n == 0:
        return oldStr
    if oldStr == "1":
        return helper("11", n - 1)
    newStr = ""
    lastIndex = 0
    for i in range(1, len(oldStr)):
        if oldStr[i] == oldStr[i-1]:
            continue
        else:
            newStr = newStr + str(i-lastIndex) + oldStr[i-1]
            lastIndex = i
    return helper(newStr + str(len(oldStr[lastIndex:])) + oldStr[lastIndex], n - 1)

def countAndSay(n):
    return helper("1", n-1)

print(countAndSay(4))
