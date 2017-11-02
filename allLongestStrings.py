def allLongestStrings(inputArray):
    x = len(inputArray)
    maxx =max(map(lambda x:len(x),inputArray))
    z = []
    for i in range(0,x):
        if len(inputArray[i]) == maxx:
            z.append(inputArray[i])
    return z
