class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: x[1])

        chosen = set()

        for l, r in intervals:

            # count how many already exist in interval
            count = 0
            for x in chosen:
                if l <= x <= r:
                    count += 1

            # add from right if needed
            add = []
            val = r

            while count < 2:
                if val not in chosen:
                    chosen.add(val)
                    add.append(val)
                    count += 1
                val -= 1

        return len(chosen)