class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ''' 
        N1 = [1,2,3,2,1]
              ^
        N2 = [3,2,1,4,7]
                ^
        This is offset technique, starting from both array
        Time - 0(n^2)
        space - o(1)
        '''
        def findL(nums1, nums2):
            N1 = len(nums1)
            N2 = len(nums2)
            best = 0
            for j in range(N2):
                counter = 0
                for i in range(N1):
                    if j + i >= N2:
                        break
                    if nums1[i] == nums2[j + i]:
                        counter += 1
                        best = max(best, counter)
                    else:
                        counter = 0
            return best
        return max(findL(nums1, nums2), findL(nums2, nums1))