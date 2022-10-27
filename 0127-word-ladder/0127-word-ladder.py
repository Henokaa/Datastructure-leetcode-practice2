class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        que = collections.deque([[beginWord, 1]])
        graph = defaultdict(list)
        # it's not wise to draw a graph
        
        while que:
            tempword, level = que.popleft()
            if tempword == endWord:
                return level
            for i in range(len(tempword)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextword = tempword[:i] + c + tempword[i+1:]
                    if nextword in wordList:
                        wordList.remove(nextword)  # very important otherwise TLE
                        que.append((nextword, level + 1))
                    
        return 0
            
    
        # visit = set([beginWord])
        # q = deque([beginWord])
        # res = 1
        # while q:
        #     for i in range(len(q)):
        #         word = q.popleft()
        #         if word == endWord:
        #             return res
        #         for j in range(len(word)):
        #             pattern = word[:j] + "*" + word[j + 1 :]
        #             for neiWord in nei[pattern]:
        #                 if neiWord not in visit:
        #                     visit.add(neiWord)
        #                     q.append(neiWord)
        #     res += 1
        # return 0
        