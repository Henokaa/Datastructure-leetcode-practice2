from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.bookings = SortedList()
    
    def book(self, start: int, end: int) -> bool:
        # check if there is any overlap with an existing booking
        i = self.bookings.bisect_right((start,end))
        if i > 0 and self.bookings[i-1][1] > start:
            return False
        if i < len(self.bookings) and end > self.bookings[i][0]:
            return False
        
        # insert the new booking at the correct position
        self.bookings.add((start, end))
        return True

        

# brute force
'''
In this implementation, we use a SortedList object to store the bookings. The SortedList automatically keeps the elements in sorted order, so we don't need to call the .sort() method as we did in the previous implementations.

To check if there is any overlap with an existing booking, we use the bisect_right method of the SortedList object to find the correct position to insert the new booking. If there is any overlap with the previous or next booking, we return False.

The time complexity of this approach is O(nlogn) for each booking because the bisect_right method has a time complexity of O(logn), and we call it twice for each booking. The space complexity is O(n) to store the bookings in a SortedList.
'''
