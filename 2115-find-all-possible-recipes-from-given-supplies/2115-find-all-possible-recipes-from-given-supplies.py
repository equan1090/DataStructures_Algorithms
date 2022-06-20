class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
                yeast  flour
                   \   /
         meat      bread
            \      /
              sandwich
                  
                  
        graph = {
            yeast: [bread]
            flour: [bread]
            meat: [sandwich]
            bread: [sandwich]
        }
        numParents = {
            bread = 2
            sandwich = 2
        }
        recipes =        ["bread",         "sandwich"], 
        ingredients = [["yeast","flour"],["bread","meat"]], 
        supplies = ["yeast","flour","meat"]
    
        '''
        graph = defaultdict(list)
        numParents = defaultdict(int)
        
        for rec, ing in zip(recipes, ingredients):
            for i in ing:
                numParents[rec] += 1
                graph[i].append(rec)
        
        q = deque(supplies)
        res = []
        while q:
            node = q.popleft()
            if node in recipes:
                res.append(node)
            
            for child in graph[node]:
                numParents[child] -= 1
                if numParents[child] == 0:
                    q.append(child)
        return res
            
            