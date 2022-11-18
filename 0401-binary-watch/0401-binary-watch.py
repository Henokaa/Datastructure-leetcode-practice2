class Solution(object):    
    def readBinaryWatch(self, num):
        def dfs(LEDS, idx, hrs, mins, n):
            
            
            if hrs >= 12 or mins >= 60:
                return
            if n == 0:
                time = str(hrs) + ":" + "0"*(mins<10) + str(mins)
                result.append(time)
                return

            if idx < len(LEDS):
                if idx <= 3:  
                    dfs(LEDS, idx+1, hrs + LEDS[idx], mins, n-1)
                else:  
                    dfs(LEDS, idx+1, hrs, mins + LEDS[idx], n-1)
                dfs(LEDS, idx+1, hrs, mins, n)
        result = []
        LEDS = [
            8, 4, 2, 1,  
            32, 16, 8, 4, 2, 1 
        ]
        dfs(LEDS, 0, 0, 0, num)
        
        return result