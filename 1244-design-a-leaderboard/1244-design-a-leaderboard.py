class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        
    # O(1)
    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
        
    # We're limiting the heap to just K items. So it's O(N log K).
    def top(self, K: int) -> int:
        heap = []
        for score in self.scores.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        
        return sum(heap)
    
    # O(1)
    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]    
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)