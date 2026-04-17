class Solution:
    def robotSim(self, commands, obstacles):
        obs = set(map(tuple, obstacles))

        # North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # start facing north

        x = y = 0
        max_dist = 0

        for c in commands:

            if c == -1:  # right turn
                d = (d + 1) % 4

            elif c == -2:  # left turn
                d = (d - 1) % 4

            else:
                dx, dy = dirs[d]

                for _ in range(c):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obs:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x * x + y * y)

        return max_dist