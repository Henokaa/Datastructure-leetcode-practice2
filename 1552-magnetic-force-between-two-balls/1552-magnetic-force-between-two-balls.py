class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions
        position.sort()

        def canPlaceBalls(min_dist):
            # Place the first ball at the first position
            count = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        # Binary search on the answer
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right