class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for num in w:
            total += num
            self.prefix.append(total)
            

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.prefix[-1])
        
        left, right = 0, len(self.prefix) - 1
        best = -1
        while left <= right:
            mid = (left + right) // 2
            if self.prefix[mid] >= random_num:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()