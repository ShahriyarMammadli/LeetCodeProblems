# Shahriyar Mammadli
# LeetCode problem '557. Reverse Words in a String III' solution

# def reverseWords(s):
#     result = ""
#     word = ""
#     for character in s:
#         if character != " ":
#             word = character + word
#         else:
#             result = result + word + " "
#             word = ""
#     return result + word

def reverseWords(s):
    words = s.split(" ")
    words = map(lambda x: x[::-1], words)
    return " ".join(words)


print(reverseWords("Let's take LeetCode contest"))

