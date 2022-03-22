# Shahriyar Mammadli
# LeetCode problem '917. Reverse Only Letters' solution

def reverseOnlyLetters(s):
    letters = [character for character in s if character.isalpha()]
    ans = []
    for character in s:
        if character.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(character)
    return "".join(ans)


print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))