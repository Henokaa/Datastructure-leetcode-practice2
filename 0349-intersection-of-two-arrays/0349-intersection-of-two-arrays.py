class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums1)):
            hashmap[nums1[i]] += 1
        
        hashmap2 = defaultdict(int)
        for i in range(len(nums2)):
            hashmap2[nums2[i]] += 1
        
        # print(hashmap2)
        visited = set()
        for i in range(len(nums1)):
            if nums1[i] in hashmap2:
                visited.add(nums1[i])
        
        return list(visited)
                
        
        