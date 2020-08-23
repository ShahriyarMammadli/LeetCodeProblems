# Shahriyar Mammadli
# LeetCode problem '1496. Path Crossing' solution

def isPathCrossing(path):
    # Create array of visited locations
    locArr = [(0, 0)]
    x = y = 0
    # Construct new location depending on a new location
    for i in path:
        if i == 'N':
            y = y + 1
        elif i == 'E':
            x = x + 1
        elif i == 'W':
            x = x - 1
        elif i == 'S':
            y = y - 1
        else:
            continue
        if (x,y) in locArr:
            return True
        locArr.append((x, y))
    return False

print(isPathCrossing("NESWW"))