class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        mag = {}
        for c in ransomNote:
            ransom[c] = 1 + ransom.get(c, 0)
        for c in magazine:
            mag[c] = 1 + mag.get(c, 0)
        
        for key in ransom:
            if key not in mag or mag[key] < ransom[key]:
                return False
        return True