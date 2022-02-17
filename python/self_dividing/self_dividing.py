'''
A self-dividing number is a number that is divisible by every digit it contains. For example, 128 is
a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example
Input: left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

1 2 3 4 5 6 7 8 9 10


loop through a range between left and right + 1
add single digits into an array
if num > 10 change number to string and split it,
change split strings back into numbers and use the modular operator on both
if both modular op == true append it to array

'''
def self_dividing(left, right):
    result = []
    for i in range(left, right + 1):
        if i < 10:
            result.append(i)
        else:
            value = str(i)
            divisible = True
            for char in value:
                if int(char) == 0:
                    divisible = False
                    break
                if i % int(char) != 0 :
                    divisible = False
                    break
            if divisible:
                result.append(i)
    return result

print(self_dividing(1, 100))

