# Shahriyar Mammadli
# LeetCode problem '709. To Lower Case' solution

def loLowerCase(str):
    return ''.join(list(map(lambda i: chr(97 + ord(i) - 65) if ord(i) > 64 and ord(i) < 91 else i, str)))


print(loLowerCase("Why"))