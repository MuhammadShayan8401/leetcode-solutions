class Solution:
    def numberOfSpecialChars(self, word):
        lower_last = {}
        upper_first = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower_last[ch] = i
            else:
                c = ch.lower()
                if c not in upper_first:
                    upper_first[c] = i

        count = 0

        for c in lower_last:
            if c in upper_first and lower_last[c] < upper_first[c]:
                count += 1

        return count