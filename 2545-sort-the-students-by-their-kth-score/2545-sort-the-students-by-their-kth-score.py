class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        dicc={}
        arr=[]

        for i in range(len(score)):
            arr.append(score[i][k])

        for j in range(len(score)):
            dicc[arr[j]]=score[j]

        for kk in sorted(dicc.keys(),reverse=True):
            ans.append(dicc[kk])
        
        return ans

        