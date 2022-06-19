class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        num_parents = defaultdict(int)
        
        for r, ing in zip(recipes, ingredients):
            
            for i in ing:
                num_parents[r] += 1
                graph[i].append(r)
        
        q = deque(supplies)
        res = []
        
        while q:
            node = q.popleft()
            if node in recipes:
                res.append(node)
        
            for child in graph[node]:
                num_parents[child] -= 1
                if num_parents[child] == 0:
                    q.append(child)
        return res
            