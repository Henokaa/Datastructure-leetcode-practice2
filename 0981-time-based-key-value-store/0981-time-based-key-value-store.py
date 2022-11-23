class TimeMap:
    '''
    [(1,foo): bar, (2,foo): bar]
    foo : [(foo,1), (foo,20), (foo, 30)]  
    '''

    def __init__(self):
        self.saved = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.saved[key].append((timestamp, value))
        
        # print(self.saved)
            

    def get(self, key: str, timestamp: int) -> str:
        if key in self.saved:
            temp = self.saved[key]
            if len(temp) >= 2:
                l = -1
                r = len(temp)
                while r > l + 1:
                    mid = l + (r - l)// 2
                    if temp[mid][0] == timestamp:
                        return temp[mid][1]
                    elif temp[mid][0] > timestamp:
                        r = mid
                    elif temp[mid][0] < timestamp:
                        l = mid
                if l == -1:
                    return ""
                else:
                    return temp[l][1]  
            else:
                if timestamp >= temp[0][0]:
                    return temp[0][1]
                else:
                    return ""
                
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp);