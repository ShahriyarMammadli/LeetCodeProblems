# Shahriyar Mammadli
# LeetCode problem '1078. Occurrences After Bigram' solution

def findOcurrences(text, first, second):
    # Create an empty array for third words
    outList = []
    # Firstly check if there appears first and second words sequentially
    while (first + " " + second) in text:
        # Find the starting of first and second words and...
        # ...the starting index of third word
        begIndFS = text.index(first + " " + second)
        endIndT= begIndFS + len(first + " " + second) + 1
        # There may be the case there is nothing after first and second word
        if endIndT >= len(text):
            break
        # Split the text after the first and the second word by space to obtain...
        # ...the third word
        word = text[endIndT:].split(" ")[0]
        # Make sure there is an space before the first word and after the second word
        if begIndFS == 0 and text[endIndT-1] == " ":
            outList.append(word)
        elif begIndFS > 0 and text[begIndFS - 1] == " " and text[endIndT-1] == " ":
            outList.append(word)
        text = text[endIndT:]
    return outList

print(findOcurrences("we will we will rock you", "we", "will"))
