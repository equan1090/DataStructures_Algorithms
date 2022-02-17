'''
 You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array
  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.


  [4, 1, 3, 2, 2, 2, 2, 2]
         || 
  toMove = 2
'''

def moveElementToEnd(array, toMove):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx < rightIdx:
        while leftIdx < rightIdx and array[rightIdx] == toMove:
            rightIdx -= 1
        
        if array[leftIdx] == toMove:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
        leftIdx += 1
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))