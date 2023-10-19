from collections import Counter
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_kth_largest(nums, k):
            pivot = random.choice(nums)  # Randomly select a pivot element
            larger = [x for x in nums if x > pivot]
            equal = [x for x in nums if x == pivot]
            smaller = [x for x in nums if x < pivot]

            if k <= len(larger):
                return find_kth_largest(larger, k)
            elif k <= len(larger) + len(equal):
                return pivot
            else:
                return find_kth_largest(smaller, k - len(larger) - len(equal))
            
        return find_kth_largest(nums, k)
'''
The time complexity of this optimized solution is typically O(n) on average, as it avoids sorting the entire array and only focuses on the relevant subarrays. However, in the worst-case scenario, it can still degrade to O(n^2).
'''

