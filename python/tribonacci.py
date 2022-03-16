def tribonacci(n):

    return _tribonacci(n)


def _tribonacci(n, memo={0: 0, 1: 0, 2: 1}):
    if n in memo:
        return memo[n]

    memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n -
                                                     2, memo) + _tribonacci(n - 3, memo)

    return memo[n]
