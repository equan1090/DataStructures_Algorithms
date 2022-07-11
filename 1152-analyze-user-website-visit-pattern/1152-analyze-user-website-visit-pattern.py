class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        heap = []
        for i in range(len(timestamp)):
            heapq.heappush(heap, (timestamp[i],website[i],username[i]))

        users = defaultdict(list)

        while heap:
            timeStamp,webSite,userName = heapq.heappop(heap)
            users[userName].append(webSite)

        count = defaultdict(int)
        maximum = 0
        result = tuple()

        for key in users:
            combos = combinations(users[key],3)
            for sequence in set(combos):
                count[sequence]+=1
                if count[sequence]>maximum:
                    maximum = count[sequence]
                    result = sequence              
                elif count[sequence]==maximum:
                    if sequence<result:
                        result = sequence
        return list(result)  