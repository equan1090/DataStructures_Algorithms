class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l = 0
        r = len(products) - 1
        res = []
        
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1 
            
            res.append([])
            window = r - l + 1
            for j in range(min(3, window)):
                res[-1].append(products[l + j])
        return res