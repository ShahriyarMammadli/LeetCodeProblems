# Shahriyar Mammadli
# LeetCode problem '7. Reverse Integer' solution

def reverse(x):
    # Convert integer into string to handle
    xStr = str(x)
    revRes = ''
    length = len(xStr)
    if length == 0:
        return int(x)
    while length > 0:
        revRes = revRes + xStr[length - 1]
        length = length - 1
    if revRes[0] == '0' and len(revRes) > 1:
        revRes = revRes[1:]
    if revRes[-1] == '-':
        revRes = '-' + revRes[:len(revRes)-1]
    return int(revRes) if abs(int(revRes)) <= 2147483647 else 0

print(reverse(1563847412))