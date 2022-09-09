class UndergroundSystem:

    def __init__(self):
        self.peopleCheck = {}
        self.timeCheck = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.peopleCheck:
            self.peopleCheck[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.peopleCheck:
            startStation, startTime = self.peopleCheck[id]
            del self.peopleCheck[id]
            time = t - startTime
            
            if (startStation, stationName) not in self.timeCheck:
                self.timeCheck[(startStation, stationName)] = [time, 1]
            else:
                self.timeCheck[(startStation, stationName)][0] += time
                self.timeCheck[(startStation, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        sumOfTimes, numOfTrips = self.timeCheck[(startStation, endStation)]
        
        return sumOfTimes / numOfTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)