'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def lengthOfSubstring(s):
    longest = 0
    l = 0
    seen = set()
    for r in range(len(s)):
        curVal = s[r]
        while curVal in seen:
            seen.remove(s[l])
            l += 1
        longest = max(longest, r - l + 1)
        seen.add(curVal)
