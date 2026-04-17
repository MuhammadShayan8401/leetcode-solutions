class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)

        mod1 = []
        mod2 = []

        for num in nums:
            if num % 3 == 1:
                mod1.append(num)
            elif num % 3 == 2:
                mod2.append(num)

        mod1.sort()
        mod2.sort()

        remainder = total % 3

        if remainder == 0:
            return total

        if remainder == 1:
            remove1 = mod1[0] if len(mod1) >= 1 else float('inf')
            remove2 = mod2[0] + mod2[1] if len(mod2) >= 2 else float('inf')
            return total - min(remove1, remove2)

        if remainder == 2:
            remove1 = mod2[0] if len(mod2) >= 1 else float('inf')
            remove2 = mod1[0] + mod1[1] if len(mod1) >= 2 else float('inf')
            return total - min(remove1, remove2)

        return 0