class UndergroundSystem:

    def __init__(self):
        self.graph = defaultdict(dict)
        self.check = defaultdict(tuple)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName,t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.check[id]
        elapsed = t - check_in_time
        prev = self.graph[check_in_station]
        time, cnt = prev[stationName] if stationName in prev else (0, 0)
        self.graph[check_in_station][stationName] = (time+elapsed, cnt+1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.graph[startStation][endStation]
        return total/cnt
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)