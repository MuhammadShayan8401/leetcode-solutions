class Solution:
    def countTrapezoids(self, points):
        from collections import defaultdict, Counter

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def line_key(x1, y1, x2, y2):
            dy = y2 - y1
            dx = x2 - x1
            g = gcd(abs(dy), abs(dx))
            dy //= g
            dx //= g
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:
                dy = 1
            c = dy * x1 - dx * y1
            return (dy, dx, c)

        n = len(points)
        slope_to_lines = defaultdict(lambda: defaultdict(list))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                lk = line_key(x1, y1, x2, y2)
                slope = (lk[0], lk[1])
                slope_to_lines[slope][lk].append((i, j))

        ans = 0

        for slope, lines in slope_to_lines.items():
            line_keys = list(lines.keys())
            if len(line_keys) < 2:
                continue

            seg_per_line = [len(lines[lk]) for lk in line_keys]
            total_segs = sum(seg_per_line)
            same_line_pairs = sum(s * (s - 1) // 2 for s in seg_per_line)
            cross_pairs = total_segs * (total_segs - 1) // 2 - same_line_pairs
            ans += cross_pairs

            freq = Counter()
            for lk in line_keys:
                for i, j in lines[lk]:
                    freq[i] += 1
                    freq[j] += 1

            same_line_overlap = 0
            for lk in line_keys:
                lfreq = Counter()
                for i, j in lines[lk]:
                    lfreq[i] += 1
                    lfreq[j] += 1
                for v in lfreq.values():
                    same_line_overlap += v * (v - 1) // 2

            total_overlap = sum(v * (v - 1) // 2 for v in freq.values())
            ans -= (total_overlap - same_line_overlap)

        # Subtract parallelograms efficiently:
        # Group pairs by midpoint, then within each midpoint group,
        # group by line_key to separate collinear from non-collinear pairs.
        midpoint_map = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                mid = (x1 + x2, y1 + y2)
                lk = line_key(x1, y1, x2, y2)
                midpoint_map[mid].append(lk)

        for mid, lk_list in midpoint_map.items():
            m = len(lk_list)
            if m < 2:
                continue

            # Count pairs on the SAME line (collinear, invalid parallelogram)
            lk_counter = Counter(lk_list)
            same_line = sum(c * (c - 1) // 2 for c in lk_counter.values())

            # Total pairs minus collinear pairs = valid parallelograms
            ans -= (m * (m - 1) // 2 - same_line)

        return ans