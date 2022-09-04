class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1
        l2 = n - 1
        p = len(nums1) - 1
        while p >= 0 and l2 >= 0:
            if l1 >= 0 and nums1[l1] >= nums2[l2]:
                nums1[p] = nums1[l1]
                p -= 1
                l1 -= 1
            else:
                nums1[p] = nums2[l2]
                p -= 1
                l2 -= 1
        
    ''''''