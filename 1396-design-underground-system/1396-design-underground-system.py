class UndergroundSystem:

    def __init__(self):
        self.personCheckIn = {}
        self.travelTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.personCheckIn:
            self.personCheckIn[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.personCheckIn:
            
            stationStart, time = self.personCheckIn.pop(id)
            

            if (stationStart, stationName) in self.travelTime:
                self.travelTime[(stationStart, stationName)][0] += t - time
                self.travelTime[(stationStart, stationName)][1] += 1
            else:
                self.travelTime[(stationStart, stationName)] = [t - time, 1]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, traveled = self.travelTime[(startStation, endStation)]
        
        return time / traveled


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)