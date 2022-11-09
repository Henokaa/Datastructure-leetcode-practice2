class Solution:
    def reorganizeString(self, s: str) -> str:
        # counter
        total = Counter(s)
        maxHeap = []
        
        for char, num in total.items():
            heapq.heappush(maxHeap, [-num, char])
        # heap
        # print(maxHeap)
        que = []
        ans = ""
        while maxHeap:
            if len(maxHeap) >= 2:
                for _ in range(2):
                    num, char = heapq.heappop(maxHeap)
                    ans += char
                    if num + 1 < 0:
                        que.append([num + 1, char])
                
                if que:
                    for n, elem in que:
                        heapq.heappush(maxHeap, [n, elem])
                        
                que = [] #  I forgot
            elif len(maxHeap) == 1:
                num, char = heapq.heappop(maxHeap)
                if num == -1:
                    return ans + char
                else:
                    return ""
                
        return ans

                    
                
            
        # 2 pop of zero not allowed
    