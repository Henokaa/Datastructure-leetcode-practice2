from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.s1 = SortedList()
        
        

    def book(self, start: int, end: int) -> bool:
        end -= 1
        index = self.s1.bisect_left((start, -1))

        
        if index < len(self.s1):
            left, right = self.s1[index]
            if left <= start <= right or left <= end <= right or start <= left <= end or start <= right <= end:
                return False
            
        if index - 1 >= 0:
            left, right = self.s1[index - 1]
            if left <= start <= right or left <= end <= right or start <= left <= end or start <= right <= end:
                return False
            
        self.s1.add((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)