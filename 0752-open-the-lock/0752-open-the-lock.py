class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        
        "0000"
        
        dead
        
        target
        
        
        
        '''
        dead = set()
        que = deque()
        que.append("0000")
        visited = set()
        visited.add("0000")
        count = 0
        for i in deadends:
            dead.add(i)
        if "0000" in dead:
            return -1
        while que:
            length = len(que)
            for i in range(length):
                elem = que.popleft()
                if elem == target:
                    return count
                
                
                temp = []
                for i in range(len(elem)):
                    if elem[i] != "0" and elem[i] != "9": 
                        change = int(elem[i]) + 1
                        number = elem[:i] + str(change) + elem[i+1:]
                        if number not in dead and number not in visited:
                            que.append(number)
                            visited.add(number)
                        
                        change = int(elem[i]) - 1
                        number = elem[:i] + str(change) + elem[i+1:]
                        if number not in dead and number not in visited:
                            que.append(elem[:i] + str(change) + elem[i+1:])
                            visited.add(number)
                        
                    else:
                        if elem[i] == "0":
                            change = "9"
                            number = elem[:i] + str(change) + elem[i+1:]
                            if number not in dead and number not in visited:
                                que.append(elem[:i] + str(change) + elem[i+1:])
                                visited.add(number)
                            
                            change = int(elem[i]) + 1
                            number = elem[:i] + str(change) + elem[i+1:]
                            if number not in dead and number not in visited:
                                que.append(elem[:i] + str(change) + elem[i+1:])
                                visited.add(number)
                            
                        elif elem[i] == "9":
                            change = int(elem[i]) - 1
                            number = elem[:i] + str(change) + elem[i+1:]
                            if number not in dead and number not in visited:
                                que.append(elem[:i] + str(change) + elem[i+1:])
                                visited.add(number)
                            
                            change = "0"
                            number = elem[:i] + str(change) + elem[i+1:]
                            if number not in dead and number not in visited:
                                que.append(elem[:i] + str(change) + elem[i+1:])
                                visited.add(number)
                    
            count += 1
        return -1