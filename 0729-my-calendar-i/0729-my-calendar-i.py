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
In this implementation, we use a SortedList object to store the bookings. The SortedList automatically keeps the elements in sorted order, so we don't need to call the .sort() method as we did in the previous implementations.

To check if there is any overlap with an existing booking, we use the bisect_right method of the SortedList object to find the correct position to insert the new booking. If there is any overlap with the previous or next booking, we return False.

The time complexity of this approach is O(nlogn) for each booking because the bisect_right method has a time complexity of O(logn), and we call it twice for each booking. The space complexity is O(n) to store the bookings in a SortedList.
'''
