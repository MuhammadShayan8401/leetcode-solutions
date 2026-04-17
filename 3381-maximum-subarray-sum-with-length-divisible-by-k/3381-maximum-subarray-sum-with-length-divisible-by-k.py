class Solution:
    def maxSubarraySum(self, nums, k):
        n = len(nums)

        prefix = 0
        ans = float('-inf')

        min_prefix = [float('inf')] * k
        min_prefix[0] = 0

        for i in range(n):
            prefix += nums[i]
            mod = (i + 1) % k

            if min_prefix[mod] != float('inf'):
                ans = max(ans, prefix - min_prefix[mod])

            min_prefix[mod] = min(min_prefix[mod], prefix)

        return ans