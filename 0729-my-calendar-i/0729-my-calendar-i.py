class MyCalendar:
    def __init__(self):
        self.bookings = []
    
    def book(self, start: int, end: int) -> bool:
        # find the correct position to insert the new booking using binary search
        left, right = 0, len(self.bookings)
        while left < right:
            mid = (left + right) // 2
            if self.bookings[mid][1] <= start:
                left = mid + 1
            elif self.bookings[mid][0] >= end:
                right = mid
            else:
                return False
        
        # insert the new booking at the correct position
        self.bookings.insert(left, (start, end))
        return True
        

# brute force
'''
def book(events, new_event) -> bool:
        for event in events:
            if new_event[0] < event[1] and new_event[1] > event[0]:
                # new event overlaps with existing event
                return False
        # no overlap found, can add the new event
        return True
'''
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)