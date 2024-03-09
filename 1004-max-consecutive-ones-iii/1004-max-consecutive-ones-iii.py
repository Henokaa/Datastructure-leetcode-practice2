class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        max_length = 0
        saved_one = 0
        while r < len(nums):
            if nums[r] == 1:
                saved_one += 1
            
            length = r - l + 1
            zeros = length - saved_one
            
            if zeros > k:
                if nums[l] == 1:
                    saved_one -= 1
                l += 1
            else:
                max_length = max(max_length, length)
                r += 1
        
        return max_length
            
        