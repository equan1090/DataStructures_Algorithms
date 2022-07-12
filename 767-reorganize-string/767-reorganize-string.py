class Solution:
    def reorganizeString(self, s: str) -> str:
        
        if not s:
            return ''
        
        res = ''
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        heap = []
        
        for key in freq:
            heapq.heappush(heap, (-freq[key], key))
        
        while len(heap) > 1:
            v1, k1 = heapq.heappop(heap)
            v2, k2 = heapq.heappop(heap)
            
            res += k1
            res += k2
            
            if abs(v1) > 1:
                heapq.heappush(heap, (v1 + 1, k1))
            if abs(v2) > 1:
                heapq.heappush(heap, (v2 + 1, k2))
        
        
        if heap:
            v1, k1 = heap[0]
            if -v1 > 1:
                return ''
            else:
                res += k1
        return res
            