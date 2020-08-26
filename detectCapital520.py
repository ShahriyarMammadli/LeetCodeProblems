# Shahriyar Mammadli
# LeetCode problem '520. Detect Capital' solution

def detectCapitalUse(word):
    if word == "":
        return True
    capital = 0
    for i in word:
        if ord(i) > 64 and ord(i) < 91:
            capital = capital + 1
    if ord(word[0]) > 64 and ord(word[0]) < 91 and capital == 1:
        return True
    if capital == len(word):
        return True
    return True if capital == 0 else False

print(detectCapitalUse("USA"))