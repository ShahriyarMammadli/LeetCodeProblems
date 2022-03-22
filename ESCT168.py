# Shahriyar Mammadli
# LeetCode problem '168. Excel Sheet Column Title' solution


def convertToTitle(columnNumber):
    title = ""
    while columnNumber > 0:
        remainder = (columnNumber - 1) % 26
        title += chr(65 + remainder)
        columnNumber = (columnNumber - 1) // 26
    return title[::-1]


print(convertToTitle(701))
