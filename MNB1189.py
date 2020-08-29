# Shahriyar Mammadli
# LeetCode problem '1189. Maximum Number of Balloons' solution

def maxNumberOfBalloons(text):
    # Remove duplicate characters from the keyword
    keyword = 'balon'
    dictArr = [0] * len(keyword)
    for i in text:
        if i in keyword:
            dictArr[keyword.index(i)] = dictArr[keyword.index(i)] + 1
    # Divide the number of 'l' and 'o' occurrences by 2 since they appear twice
    dictArr[keyword.index('l')] = int(dictArr[keyword.index('l')] / 2)
    dictArr[keyword.index('o')] = int(dictArr[keyword.index('o')] / 2)
    return min(dictArr)

print(maxNumberOfBalloons(""))
