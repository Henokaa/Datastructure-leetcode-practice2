class UndergroundSystem:
    '''
    checkin
    id: (username, time)
    
    checkout
    id: (state1, state2, time_diff)
    
    (state1, state2): [time_diff]
    
    '''

    def __init__(self):
        self.CheckIn_dict = {}
        self.CheckOut_dict = {}
        self.CheckAverage = defaultdict(list)
        
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.CheckIn_dict[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.CheckIn_dict:
            stationName_In, checkIn_time = self.CheckIn_dict[id]
            
        self.CheckOut_dict[id] = (stationName_In, stationName, t - checkIn_time) 
        
        self.CheckAverage[(stationName_In, stationName)].append(t - checkIn_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = 0
        length = len(self.CheckAverage[(startStation, endStation)])
        for averageTime in self.CheckAverage[(startStation, endStation)]:
            total  += averageTime 
        
        return total / length
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)