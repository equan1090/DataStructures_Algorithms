'''
Write a function that takes in a non-empty array of distince integers and an i
integer representing a targetSum. The function should return all triplets
in the array that sum up to the garget sum in a two-dimensional array of triplets

'''
#O(nlogn) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
    return result


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
