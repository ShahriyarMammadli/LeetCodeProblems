# Shahriyar Mammadli
# LeetCode problem '1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts' solution

# Get the distance between vertical cuts
def processVer(h, horizontalCuts, verDis):
    horizontalCuts.sort()
    verDis[0] = horizontalCuts[0]
    for i in range(1, len(horizontalCuts)):
        verDis[i] = horizontalCuts[i] - horizontalCuts[i-1]
    verDis[-1] = h - horizontalCuts[-1]
    return verDis

# Get the distance between horizontal cuts
def processHor(w, verticalCuts, horDis):
    verticalCuts.sort()
    if not len(verticalCuts) == 0:
        horDis[0] = verticalCuts[0]
    for i in range(1, len(verticalCuts)):
        horDis[i] = verticalCuts[i] - verticalCuts[i - 1]
    horDis[-1] = w - verticalCuts[-1]
    return horDis

def maxArea(h, w, horizontalCuts, verticalCuts):
    # If there is no cut then area is equal to width*height
    if len(horizontalCuts) == 0:
        if len(verticalCuts) == 0:
            return h*w
    verDis = [None] * (len(horizontalCuts) + 1)
    horDis = [None] * (len(verticalCuts) + 1)
    # Check if there is a vertical cut
    if len(horizontalCuts) > 0:
        verDis = processVer(h, horizontalCuts, verDis)
    else:
        verDis[0] = h
    # Check if there is a horizontal cut
    if len(verticalCuts) > 0:
        horDis = processHor(w, verticalCuts, horDis)
    else:
        horDis[0] = w

    return max(verDis) * max(horDis) % 1000000007
print(maxArea(5, 4, [1,2,4], [1,3]))
