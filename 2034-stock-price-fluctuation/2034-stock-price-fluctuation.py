class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.max_time = 0
        self.minHeap = []
        self.maxHeap = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.max_time = max(self.max_time, timestamp)
        
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.max_time]
        

    def maximum(self) -> int:
        curPrice, timestamp = heapq.heappop(self.maxHeap)
        while -curPrice != self.timestamps[timestamp]:
            curPrice,timestamp = heapq.heappop(self.maxHeap)
        
        heapq.heappush(self.maxHeap, (curPrice, timestamp))
        return -curPrice
    
    def minimum(self) -> int:
        curPrice, timestamp = heapq.heappop(self.minHeap)
        while curPrice != self.timestamps[timestamp]:
            curPrice, timestamp = heapq.heappop(self.minHeap)
        
        heapq.heappush(self.minHeap, (curPrice, timestamp))
        return curPrice
        
        
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()