'''
Given a string s and an integer k, return the length of the longest substring of s that contains at most
k distinct characters.

Leetcode 340
'''
from collections import defaultdict

def lengthOfLongestSubstringKDistinct(s, k):
    freq = defaultdict(int)
    longest = 0
    l = 0
    for r in range(len(s)):
        freq[s[r]] += 1
        while len(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
        longest = max(longest, r - l + 1)
    return longest
