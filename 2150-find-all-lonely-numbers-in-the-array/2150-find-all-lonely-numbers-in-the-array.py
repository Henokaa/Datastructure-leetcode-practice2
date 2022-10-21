class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        '''
        [10,6,5,8]
        
        [5, 6, 8, 10]
        
        [1, 3, 3, 5]
        
        '''
        visited = set()
        safe = set()
        answer = []
        for i in nums:
            if i in visited:
                safe.add(i)
            visited.add(i)
        for ele in nums:
            if ele+1 in visited or ele - 1 in visited or ele in safe:
                continue
            else:
                answer.append(ele)
        
        return answer
                
            
                