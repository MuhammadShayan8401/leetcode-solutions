class Solution:
    def minMirrorPairDistance(self, nums):
        index_map = {}
        min_dist = float('inf')

        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])

            # Check if current number already exists as a reversed value
            if num in index_map:
                min_dist = min(min_dist, i - index_map[num])

            # Store reversed number as key
            index_map[rev] = i

        return min_dist if min_dist != float('inf') else -1