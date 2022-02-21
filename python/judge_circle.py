'''
// Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a
circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false
representing whether the robot makes a circle.

def judge_circle(moves)
    Input: "UD"
    Output: true
    Example 2:
    Input: "LL"
    Output: false


hash {right: 1 , left: -1, up: 1, down: -1}

position = 0, 0
iterate through each moves
check moves value in hash
add appropriate value
return true if position is 0

'''

def judge_circles(moves):
    x = 0
    y = 0

    for char in moves:
        if char == 'U':
            y += 1
        elif char == 'D':
            y -= 1
        elif char == 'R':
            x += 1
        else:
            x -= 1

    return x == 0 and y == 0



