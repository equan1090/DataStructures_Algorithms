class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = Counter(ransomNote)
        magazineDict = Counter(magazine)

        
        for k in ransomNoteDict:
            if k not in magazineDict or magazineDict[k] < ransomNoteDict[k]:
                return False
        return True