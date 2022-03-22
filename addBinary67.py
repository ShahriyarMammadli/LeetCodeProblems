# Shahriyar Mammadli
# LeetCode problem '67. Add Binary' solution

def addBinary(a, b):
    if len(a) > len(b):
        b = "".join(["0"] * (len(a) - len(b))) + b
    elif len(b) > len(a):
        a = "".join(["0"] * (len(b) - len(a))) + a
    result = ""
    remainder = 0
    for index in range(len(a) - 1, -1, -1):
        total = remainder + int(a[index]) + int(b[index])
        if total == 0:
            result += "0"
            remainder = 0
        elif total == 1:
            result += "1"
            remainder = 0
        elif total == 2:
            result += "0"
            remainder = 1
        elif total == 3:
            result += "1"
            remainder = 1
        else:
            return None
    return result[::-1] if remainder == 0 else "1" + result[::-1]

print(addBinary("1010", "1011"))