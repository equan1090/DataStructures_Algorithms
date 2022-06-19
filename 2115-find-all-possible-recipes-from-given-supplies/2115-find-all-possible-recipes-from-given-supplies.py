class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
                yeast  flour
                    \  /
              meat  bread
                 \  /
               sandwich
        '''
        
        '''
        graph {
            yeast: [bread],
            flour: [bread],
            meat: [sandwich]
            bread: [sandwich]
            sandwich: []
        }
        num_parents = {
            bread: 2
            sandwich: 2
        }
        Input: recipes = ["bread",          "sandwich"], 
        
        ingredients = [["yeast","flour"],["bread","meat"]], 
        supplies = ["yeast","flour","meat"]
        
        '''
        graph = defaultdict(list)
        num_parents = defaultdict(int)
        
        for r, ing in zip(recipes, ingredients):
            for i in ing:
                graph[i].append(r)
                num_parents[r] += 1
        
        
        q = deque(supplies)
        res = []
        # q = [yeast, flour, meat]
        while q:
            node = q.popleft()
            
            if node in recipes:
                res.append(node)
            
            for child in graph[node]:
                num_parents[child] -= 1
                if num_parents[child] == 0:
                    q.append(child)
        return res
            
            
        
        