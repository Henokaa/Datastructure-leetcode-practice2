class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        bulf graph
         dfs(i, visited, stack)
        '''
        end = len(graph) - 1
        answer = []
        graph_2 = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                graph_2[i].append(graph[i][j])
        
        
            
        def dfs(i, stack, visited):

            for child in graph[i]:
                if child == end:
                    stack2 = stack.copy()
                    stack2.append(child)
                    answer.append(stack2)
                elif child not in visited:
                    stack.append(child)
                    visited.add(child)
                    dfs(child, stack, visited)
                    visited.remove(child)
                    stack.pop()
                
        
        dfs(0, [0], set([0]))
        return answer
        