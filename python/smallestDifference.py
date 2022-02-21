'''
Write a function that takes in two non-empty arrays of integers, finds the
pair of numbers (one from each array) whose absolute difference is closest to
zero, and returns an array containing these two numbers, with the number from
the first array in the first position.
'''
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    oneIdx, twoIdx = 0, 0
    current = float('inf')
    smallest = float('inf')
    result = []
    while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
        firstNum = arrayOne[oneIdx]
        secondNum = arrayTwo[twoIdx]
        if firstNum < secondNum:
            current = secondNum - firstNum
            oneIdx += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            twoIdx += 1
        else:
            return [firstNum, secondNum]
        
        if smallest > current:
            smallest = current
            result = [firstNum, secondNum]
    return result


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))


'''
questions
can the integers in the arrays be negative?
can i assume the arrays lengths are the same?


i would first sort both arrays
make a pointer that points to the first value for each array
make a current and smallest variable

'''