class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = {}
        magazineDict = {}
        for c in ransomNote:
            ransomNoteDict[c] = 1 + ransomNoteDict.get(c, 0)
        
        for c in magazine:
            magazineDict[c] = 1 + magazineDict.get(c, 0)
        
        print(ransomNoteDict)
        print(magazineDict)
        
        for k in ransomNoteDict:
            if k not in magazineDict or magazineDict[k] < ransomNoteDict[k]:
                return False
        return True