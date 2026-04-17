class Solution:
    def countPalindromicSubsequence(self, s):
        first = {}
        last = {}

        n = len(s)

        # record first and last positions
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        result = 0

        # check each character as outer palindrome char
        for ch in first:
            l = first[ch]
            r = last[ch]

            if r - l < 2:
                continue

            middle_chars = set(s[l+1:r])
            result += len(middle_chars)

        return result