class Leaderboard:

    def __init__(self):
        self.cache = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.cache:
            self.cache[playerId] = 0
        self.cache[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for val in self.cache.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        del self.cache[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)