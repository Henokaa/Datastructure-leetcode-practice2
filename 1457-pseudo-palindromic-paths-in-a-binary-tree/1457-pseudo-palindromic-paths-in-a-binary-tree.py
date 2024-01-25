class Solution:
    def pseudoPalindromicPaths(self, root):
        def is_pseudo_palindrome(counter):
            odd_count = 0
            for count in counter.values():
                if count % 2 != 0:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True
        
        def dfs(node, counter):
            if not node:
                return 0
            
            counter[node.val] += 1
            if not node.left and not node.right:
                result = int(is_pseudo_palindrome(counter))
            else:
                result = dfs(node.left, counter) + dfs(node.right, counter)
            
            counter[node.val] -= 1
            if counter[node.val] == 0:
                del counter[node.val]
            
            return result
        
        return dfs(root, Counter())