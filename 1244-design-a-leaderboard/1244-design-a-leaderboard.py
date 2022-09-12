class Leaderboard:

    def __init__(self):
        self.player = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.player:
            self.player[playerId] = 0
        self.player[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        
        for val in self.player.values():
            heapq.heappush(heap, val)
            
            if len(heap) > K:
                heapq.heappop(heap)
               
        
        return sum(heap)
            

    def reset(self, playerId: int) -> None:
        del self.player[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)