class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)

        robots = list(zip(positions, healths, directions, range(n)))
        robots.sort()

        stack = []
        result = [-1] * n

        for pos, health, dirc, idx in robots:

            if dirc == 'R':
                stack.append([health, idx])
            else:
                curr_health = health

                while stack and curr_health > 0:
                    top_health, top_idx = stack[-1]

                    if top_health < curr_health:
                        stack.pop()
                        curr_health -= 1

                    elif top_health > curr_health:
                        stack[-1][0] -= 1
                        curr_health = 0

                    else:
                        stack.pop()
                        curr_health = 0

                if curr_health > 0:
                    result[idx] = curr_health

        # remaining right-moving robots survive
        for h, idx in stack:
            result[idx] = h

        return [h for h in result if h != -1]