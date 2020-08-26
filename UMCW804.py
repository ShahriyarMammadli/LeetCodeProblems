# Shahriyar Mammadli
# LeetCode problem '804. Unique Morse Code Words' solution

def toMorse(str):
    morseDict = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    return ''.join(list(map(lambda i: morseDict[ord(i) - 97],str)))


def uniqueMorseRepresentations(words):
    morseList = []
    for word in words:
        morseList.append(toMorse(word))
    return len(set(morseList))

print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))