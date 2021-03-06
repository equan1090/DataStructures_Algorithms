class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)
        dic = {}
        
        for word in words:
            dic[ word ] = 1
            
            for j in range(len(word)):
                
                # creating words by deleting a letter
                pre = word[:j] + word[j+1:]
                if pre in dic:
                    dic[ word ] = max (dic[word], 1 + dic[pre])
        
        res = max(dic.values())
        return res