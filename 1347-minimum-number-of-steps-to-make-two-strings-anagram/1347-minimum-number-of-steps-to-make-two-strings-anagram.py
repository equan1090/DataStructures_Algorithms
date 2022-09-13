class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo = collections.defaultdict(int)
        # saving the number of occurance of characters in s
        for char in s:
            memo[char] += 1
			
        count = 0
        for char in t:
            if memo[char]:
                memo[char] -=1   # if char in t is also in memo, substract that from the counted number
            else:
                count += 1
       
        return count
    
    '''
    memo = {l: 1
            e: 3
            t: 1
            c: 1
            o: 1
            d: 1}
    '''