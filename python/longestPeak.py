'''
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array taht are strictly increasing until they reach a tip at which
point they become strictly decreasing. At least three integers are required to form a peak.

'''


def longestPeak(array):
    # Write your code here.
    longestPeak = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2

        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        if currentPeakLength > longestPeak:
            longestPeak = currentPeakLength
        i = rightIdx
    return longestPeak
