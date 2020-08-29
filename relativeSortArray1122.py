# Shahriyar Mammadli
# LeetCode problem '1122. Relative Sort Array' solution

def relativeSortArray(arr1, arr2):
    # Create a dictionary array in length of arr2 so that...
    # ...we can count the number of occurrences of values in...
    # ...this list
    dictArr = [0] * len(arr2)
    # Array for the values that do not occur in arr2
    remArr = []
    # Array to hold sorted list of values accroding to arr2
    resArr = []
    # If a value is in arr2 increase the count of that value...
    # ...by 1 depending on the order of that value in arr2...
    # ...thus we can ensure that values are sorted in the order...
    # ...of arr2. If value is not in arr2 add it to remArr...
    # to sort it later
    for i in arr1:
        if i in arr2:
            dictArr[arr2.index(i)] = dictArr[arr2.index(i)] + 1
        else:
            remArr.append(i)
    # Created the sorted array of values according to their...
    # ...order in arr2
    for i in range(len(dictArr)):
        for j in range(dictArr[i]):
            resArr.append(arr2[i])
    remArr.sort()
    # Merge two arrays
    return resArr + remArr

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))