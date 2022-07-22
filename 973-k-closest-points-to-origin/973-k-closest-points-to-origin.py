class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = 0
        count = {}
        answer = []
        for i in range(len(points)):
            for j in range(len(points[0])):
                x += points[i][j] ** 2

            count[i] = x
            x = 0
        
        sortcount = sorted(count.items(), key = lambda x: x[1])
        
        for i in range(len(sortcount)):
            if len(answer) == k:
                return answer
            answer.append(points[sortcount[i][0]])
        return answer
            
    
            
        