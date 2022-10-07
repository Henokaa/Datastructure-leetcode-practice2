class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        [[1,2],[2,4],[3,2],[4,1]]
        
        [1,2]
         ^
         t= 0
         que = ([1,2],0)
         
         t = 3
         
         que = [2,4],[3,2]
         
         t = 5
         
         que = [2,4], [4, 1]
         
         
         
         0 - 1
         1 - 3
        [2, 4]
        que = [1,2]
        [[2, 4], [3, 2]]
        
        [[1,2],[2,4],[3,2],[4,1]]
        t = 1
        heap([1,2])
        heapq.heappop([1,2])
        
        t = 3
        heapq.heap([2,4],[3,2])
        heapq.heapop([3,2])
        
        t = 5
        0(nlogn)
        '''
        for i, element  in enumerate(tasks):
            element.append(i) # because we will sort it the true position will change we need to save before we do
            
        tasks.sort(key = lambda x: x[0])
        i = 0
        t = tasks[i][0]
        heap = []
        answer = []
        print(tasks)
        while i < len(tasks) or heap:
            while i < len(tasks) and t >= tasks[i][0]:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if heap:
                procTime, index = heapq.heappop(heap)
                answer.append(index)
                t += procTime
            else:
                t = tasks[i][0]
        return answer
                
            
        
            