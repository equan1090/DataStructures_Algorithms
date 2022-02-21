'''
Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a funciton that
returns the first integer that appears more than once (where the array is read from left to right)

In other words, out of all the integers that occure more than once in the array, your function shouls return the duplicate
at the minimum index

You are allowed to mutate the array
'''

#array = [2, 1, 5, 2, 3, 3, 4]

# O(n) Time | O(1) space


def firstDuplicateValue(array):

    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1


# O(n) Time | O(n) Space
# def firstDuplicateValue(array):
#     values = set()

# 	for num in array:
# 		if num in values:
# 			return num
# 		values.add(num)

#     return -1
