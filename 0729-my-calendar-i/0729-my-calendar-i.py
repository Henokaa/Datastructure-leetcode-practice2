from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.bookings = []
    def book(self, start: int, end: int) -> bool:
        l = -1
        r = len(self.bookings)
        while r > l + 1:
            mid = (l + r)//2
            if self.bookings[mid][0] > start:
                r = mid
            elif self.bookings[mid][0] <= start :
                l = mid
            
        # print(self.bookings, l , r, (start, end))
        if r < len(self.bookings) and self.bookings[r][0] < end:
            # print("a")
            return False
        
        if l != -1 and self.bookings[l][0] < end and self.bookings[l][1] > start:
            # print("b")
            return False
        # if l == -1:
        #     l = 0
        self.bookings.insert(l + 1,(start, end))
        return True
            
        

        

# brute force
'''
The book method first performs a binary search on the intervals list to find the correct position to insert the new event. The time complexity of the binary search is O(log N), where N is the number of existing events in the calendar. Once the correct position is found, the method checks if the new event conflicts with any existing events. This can be done in constant time by comparing the start and end times of the new event with the intervals adjacent to it in the list. Finally, if the new event does not conflict with any existing events, it is inserted into the list in O(N) time, where N is the number of existing events. Overall, the time complexity of the book method is O(log N) for the binary search, plus O(N) for the insertion step, for a total time complexity of O(N).
'''
