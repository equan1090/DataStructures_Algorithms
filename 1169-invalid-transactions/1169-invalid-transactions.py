class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        
        memo = collections.defaultdict(list)
        invalid_tran = set()
        for i, transaction in enumerate(transactions):
            name, time, amount, city = (int(i) if i.isnumeric() else i for i in transaction.split(','))
            
            if amount > 1000:
                invalid_tran.add((transaction, i))               
                 
            if name in memo:
                for tran, idx in memo[name]:
                    _, prev_time, _, prev_city = (int(i) if i.isnumeric() else i for i in  tran.split(','))
                    if abs(time-prev_time) <= 60 and prev_city != city:
                        invalid_tran.add((tran, idx))
                        invalid_tran.add((transaction, i))                    
            
            memo[name].append((transaction, i))
        return [ele[0] for ele in invalid_tran]