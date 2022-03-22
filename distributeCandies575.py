# Shahriyar Mammadli
# LeetCode problem '575. Distribute Candies' solution

def distributeCandies(candyType):
    return min(len(set(candyType)), len(candyType) / 2)

print(distributeCandies([1,1,2,3]))