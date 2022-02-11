# Given an array of positive integers represetning the values of coins in your possession, write a function that returns
# the minimum amount of change that you cannot create. The given coins can have positive integer value and aren't
# necessarily unique.

def nonCunstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin
    return currentChange + 1
