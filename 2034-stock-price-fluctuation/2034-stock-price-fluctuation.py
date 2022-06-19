class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.newest = 0
        self.minheap = []
        self.maxheap = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.newest = max(self.newest, timestamp)
        heapq.heappush(self.minheap, (price, timestamp))
        heapq.heappush(self.maxheap, (-price, timestamp))
        

    def current(self) -> int:
        return self.timestamps[self.newest]
        

    def maximum(self) -> int:
        curPrice, timestamp = heapq.heappop(self.maxheap)
        
        while -curPrice != self.timestamps[timestamp]:
            curPrice, timestamp = heapq.heappop(self.maxheap)
        
        heapq.heappush(self.maxheap, (curPrice, timestamp))
        return -curPrice

    def minimum(self) -> int:
        curPrice, timestamp = heapq.heappop(self.minheap)
        
        while curPrice != self.timestamps[timestamp]:
            curPrice, timestamp = heapq.heappop(self.minheap)
            
        heapq.heappush(self.minheap, (curPrice, timestamp))
        return curPrice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()