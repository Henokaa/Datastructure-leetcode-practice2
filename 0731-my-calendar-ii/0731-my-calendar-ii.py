class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        overlaps = []
        for s, e in self.events:
            if start < e and s < end:
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                for o_s, o_e in overlaps:
                    if overlap_start < o_e and o_s < overlap_end:
                        # Triple booking
                        return False
                overlaps.append((overlap_start, overlap_end))
        self.events.append((start, end))
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)