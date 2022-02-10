# Given two non-empty binary arrays of integers, write a function that determines whether the second array
# is a subsequence of the first one.
# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but are in the same order
# as they appear in the array

#O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    sqxIdx = 0
    for val in array:
        if sqxIdx == len(sequence):
            break
        if val == sequence[sqxIdx]:
            sqxIdx += 1

    return len(sequence) == sqxIdx

