class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        [1,1, 4, 2,3],   x = 5
        
        '''
        r = 0
        total = 0
        flag = 0
        ans = float('inf')
        while r < len(nums):
            total += nums[r]
            if total == x:
                ans = r + 1
            if total < x:
                r += 1
            elif total >= x:
                total -= nums[r]
                r -= 1
                flag = 1
                break
                
        if flag == 0:
            print('a')
            return -1
        # print(total, r, ans)
        l = len(nums) - 1
        while True:
            # print(total)
            if total <= x:
                total = total + nums[l]
                if total == x:
                    ans = min(ans, len(nums) - l + r + 1)
                    # print("a",ans, l, r)
                l -= 1
            elif total > x:
                total = total - nums[r]
                if total == x:
                    ans = min(ans, len(nums) - l - 1 + r + 1 - 1)
                    # print("a",ans, l, r)
                if r == -1:
                    break
                r -= 1
                
        if ans != float('INF'):
            return ans
        else:
            return -1
                