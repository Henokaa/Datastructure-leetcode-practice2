class UndergroundSystem:
    '''
    45 : (leython,3), (waterloo,15)
    32: (paradise, 8), ("Cambridge", 22)
    27: (leython,10), (waterloo,20)
    10: ("Leyton", 24), ("Waterloo", 38)
    
    
    (leython,waterloo): [14, 12,10]
    
    
'''

    def __init__(self):
        self.person = defaultdict(list)
        self.station = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.person[id].append((stationName, t))
        
        start = self.person[id][-2][1]
        end = self.person[id][-1][1] 
        
        startStation = self.person[id][-2][0]
        
        self.station[(startStation, stationName)].append(end - start)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = sum(self.station[(startStation, endStation)])
        length = len(self.station[(startStation, endStation)])
        # print(total//length)
        return total / length


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)