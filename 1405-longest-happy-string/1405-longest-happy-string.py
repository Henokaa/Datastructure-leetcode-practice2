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
            if len(maxHeap) >= 2 and maxHeap[0][0] <= -2:
                # 2 pop by -2 and -1
                
                if ans and maxHeap[0][1] != ans[-1] or not ans:
                    letters, char = heapq.heappop(maxHeap)
                    if letters + 2 < 0:
                        temp.append((letters + 2, char)) 
                    ans += char + char
                
                    letters, char = heapq.heappop(maxHeap)
                    ans += char
                    if letters + 1 < 0:
                        temp.append((letters + 1, char))
                        
                elif ans and maxHeap[0][1] == ans[-1]:
                    letters, char = heapq.heappop(maxHeap)
                    
                    ans += char
                    if letters + 1 < 0:
                        temp.append((letters + 1, char))
                        
                        
                # from que append to the maxHeap
                for x, y in temp:
                    if x >= 0:
                        continue
                    heapq.heappush(maxHeap, (x, y))
                temp = []
                
                
                
            elif len(maxHeap) == 1 and maxHeap[0][0] <= -2:
                ans += maxHeap[0][1]
                ans += maxHeap[0][1]
                break
            
            while maxHeap and maxHeap[0][0] == -1:
                letters, char = heapq.heappop(maxHeap)
                ans += char
                
                
            
                
        return ans
                
                
                
        
        