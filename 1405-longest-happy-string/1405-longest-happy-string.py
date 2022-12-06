class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        a = 1, b = 1, c = 7
        
        c : 2
        a : 1
        b : 0
        
        ccaccbcc
        
        cca
        
        a : 1
        b : 1
    
        
        aab
        '''
        
        maxHeap = []
        if a != 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b != 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c != 0:
            heapq.heappush(maxHeap, (-c, 'c'))
        
        '''
        c: 3
        ccaccb
        
        
        a: 2
        b: 3
        c: 3
        
        aab
        '''
        temp = []
        ans = ""
        while maxHeap:
            # print(maxHeap, ans)
            if maxHeap and len(ans) >= 2 and ans[-1] == ans[-2] == maxHeap[0][1]:
                freq, char = heapq.heappop(maxHeap)
                temp.append((freq, char))
                
                if maxHeap:
                    freq, char = heapq.heappop(maxHeap)
                    ans += char
            
                    if freq + 1 < 0:
                        heapq.heappush(maxHeap, (freq + 1, char))
                    for x, y in temp:
                        heapq.heappush(maxHeap, (x,y))
                    temp = []
                else:
                    break
                
            else:
                freq, char = heapq.heappop(maxHeap)
                # print(freq, char)
                ans += char
                if freq + 1 < 0:
                    heapq.heappush(maxHeap, (freq + 1, char))
        return ans
                    
                # 2 pop by -2 and -1
                
                
                 
                
                
                
        
        