'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
'''

def isAnagram(string1, string2):
    return count(string1) == count(string2)

def count(string):
    seen = {}
    for char in string:
        if char not in seen:
            seen[char] = 0
        seen[char] += 1
    return seen

print(isAnagram('happy', 'ppahy'))
