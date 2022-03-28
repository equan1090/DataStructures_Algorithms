'''
Write a function, counting_change, that takes in an amount and a list of coins.
The function should return the number of different ways it is possible to make change for the given
amount using the coins.

You may reuse a coin as many times as necessary
'''

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]

  if amount == 0:
    return 1

  if i == len(coins):
    return 0

  coin = coins[i]

  total_count = 0
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_count += _counting_change(remainder, coins, i + 1, memo)

  memo[key] = total_count
  return total_count
