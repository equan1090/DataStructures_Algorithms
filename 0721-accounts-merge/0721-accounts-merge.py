class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        
        
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                em_graph[acc[1]].add(email)
                
                #connect 2nd to 1st email
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
        # dfs function
        def dfs(s,comp):
            if s in seen:
                return
            seen.add(s)
            comp.append(s)
            for nei in em_graph[s]:
                if nei not in seen:
                    dfs(nei,comp)    
            return comp  
        
        # here we use loop to traverse all unconnected
        # components of the graph
        for email in em_graph:
            if email not in seen:
                component = []
                dfs(email, component)
                ans.append([em_to_name[email]] + sorted(component))
                
        return ans      