class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        ans = 0

        # Compare with first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                ans = i
                break

        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)
                break

        return ans