class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            order = [0] * 26
            for c in word:
                order[ord(c) - ord('a')] += 1
            
            key = tuple(order)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return groups.values()
            