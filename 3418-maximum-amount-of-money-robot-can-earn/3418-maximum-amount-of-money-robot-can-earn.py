class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])

        dp = [[[-10**18] * 3 for _ in range(n)] for _ in range(m)]

        # start cell
        val = coins[0][0]

        for k in range(3):
            if val >= 0:
                dp[0][0][k] = val
            else:
                if k == 0:
                    dp[0][0][k] = val
                else:
                    dp[0][0][k] = 0  # neutralize first cell if allowed

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                val = coins[i][j]

                for k in range(3):

                    best = -10**18

                    # from top
                    if i > 0:
                        best = max(best, dp[i-1][j][k])

                    # from left
                    if j > 0:
                        best = max(best, dp[i][j-1][k])

                    if best == -10**18:
                        continue

                    # case 1: normal gain/loss
                    dp[i][j][k] = max(dp[i][j][k], best + val)

                    # case 2: neutralize if negative and k > 0
                    if val < 0 and k > 0:
                        best_prev = -10**18

                        if i > 0:
                            best_prev = max(best_prev, dp[i-1][j][k-1])
                        if j > 0:
                            best_prev = max(best_prev, dp[i][j-1][k-1])

                        if best_prev != -10**18:
                            dp[i][j][k] = max(dp[i][j][k], best_prev)

        return max(dp[m-1][n-1])