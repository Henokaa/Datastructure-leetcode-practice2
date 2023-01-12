class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums.sort()
        score = 0
        while k != 0:
            temp = nums.pop()
            score += temp
            val = math.ceil(temp / 3)
            nums.insert(bisect.bisect(nums, val), val)
            k -= 1
        return score