class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        saved = defaultdict(int)
        
        for i in s:
            saved[i] += 1
            
        # print(saved)
        
        heap = []
        
        for x,y in saved.items():
            heapq.heappush(heap, [-y, x])
        
        ans = ""
        while heap:
            freq, char = heapq.heappop(heap)
            ans += char * abs(freq)
        return ans