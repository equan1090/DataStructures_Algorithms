# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a
# new array of the same length with the squares of the original also sorted in ascending order


#O(n) time | O(n) space
def sortedSquaredArray(arr):
    result = [0 for _ in arr]
    leftIdx = 0
    rightIdx = len(arr) - 1

    for idx in reversed(range(len(result))):
        small = arr[leftIdx]
        large = arr[rightIdx]

        if abs(small) > abs(large):
            result[idx] = small**2
            leftIdx += 1
        else:
            result[idx] = large**2
            rightIdx -= 1
    return result

#O(nlogn) time | O(n) space
# def sortedSquaredArray(arr):
#     sorted = []
#     for num in arr:
#         sorted.push(num**2)
#     sorted.sort()
#     return sorted
