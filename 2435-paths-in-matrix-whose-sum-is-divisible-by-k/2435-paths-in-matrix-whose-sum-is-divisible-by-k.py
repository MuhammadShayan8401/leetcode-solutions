class Solution:
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[j][r] = ways at column j with remainder r
        dp = [[0] * k for _ in range(n)]

        # start
        dp[0][grid[0][0] % k] = 1

        for i in range(m):
            new_dp = [[0] * k for _ in range(n)]

            for j in range(n):
                for r in range(k):
                    if i == 0 and j == 0:
                        new_dp[0][r] = dp[0][r]
                        continue

                    val = grid[i][j]

                    # from top
                    if i > 0:
                        prev_r = (r - val) % k
                        new_dp[j][r] += dp[j][prev_r]

                    # from left
                    if j > 0:
                        prev_r = (r - val) % k
                        new_dp[j][r] += new_dp[j-1][prev_r]

                    new_dp[j][r] %= MOD

            dp = new_dp

        return dp[n-1][0]