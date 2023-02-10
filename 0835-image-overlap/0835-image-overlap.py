class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Build a list of coordinates of 1s in img1
        ones = []
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j]:
                    ones.append((i, j))
                    
        maxOverlap = 0
        # Double for loop from -n to n
        for i in range(-len(img1) + 1, len(img1)):
            for j in range(-len(img1) + 1, len(img1)):
                overlap = 0
                for x, y in ones:
                    # For each 1 in img1, check if the translated coordinate is within
                    # the boundaries of img2, and then check if it lines up with a 1 in img2
                    if 0 <= x+i and x+i < len(img2) and 0 <= y+j and y+j < len(img2) and img2[x+i][y+j]:
                        overlap += 1
                # Update maxOverlap
                maxOverlap = max(maxOverlap, overlap)
                
        return maxOverlap
        