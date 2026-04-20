class Solution:
    def countTrapezoids(self, points):
        MOD = 10**9 + 7

        from collections import defaultdict
        y_map = defaultdict(int)

        for x, y in points:
            y_map[y] += 1

        # Compute number of pairs per y
        pairs = []
        for count in y_map.values():
            if count >= 2:
                pairs.append(count * (count - 1) // 2)

        total = sum(pairs) % MOD

        # Use formula: (sum^2 - sum of squares) / 2
        sum_sq = sum(p * p for p in pairs) % MOD

        result = (total * total - sum_sq) % MOD
        result = result * pow(2, MOD - 2, MOD) % MOD  

        return result