# Shahriyar Mammadli
# LeetCode problem '500. Keyboard Row' solution

def rowWord(word):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    # Find the set that first character of the word belongs to and check...
    # ...if all other character are also in that set
    tempRow = row1 if word[0].lower() in row1 else(row2 if word[0].lower() in row2 else row3)
    for i in word:
        if not i.lower() in tempRow:
            return False
    return True

def findWords(words):
    resWords = []
    for word in words:
        if rowWord(word):
            resWords.append(word)
    return resWords

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))