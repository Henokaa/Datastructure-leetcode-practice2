class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}
        # print(last_occurrence)
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
            # print(stack, seen)

        return ''.join(stack)
    '''
    bca  -> a removed every one
    '''
