class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.eow = True
        
#     def search(self, word):
#         cur = self.root
#         for char in word:
#             if char not in cur.children:
#                 return False
#             cur = cur.children[char]
#         return cur.eow
    
    
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        
        for i in range(len(text)):
            node = trie.root
            
            for j in range(i, len(text)):
                cur = text[j]
                if cur in node.children:
                    node = node.children[cur]
                else:
                    break
                if node.eow:
                    res.append([i, j])
        return res