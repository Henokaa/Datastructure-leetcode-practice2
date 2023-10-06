class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for x,y in self.overlaps:
            if start < y and end > x:
                return False
            
        for s,e in self.calendar:
            if start < e and end > s:
                self.overlaps.append([max(start,s), min(end,e)])
        
        self.calendar.append([start,end])
        return True
        



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)