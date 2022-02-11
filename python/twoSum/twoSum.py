# Write a function that takes in a non-empy array of distince integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
# if no two numbers sum up to the target sum, the function should return an empty array

#O(n) time and space
def twoNumberSum(array, targetSum):
    my_dict = {}

    for val in array:
        compliment = targetSum - val
        if compliment in my_dict:
            return [compliment, val]
        my_dict[val] = True
    return []
