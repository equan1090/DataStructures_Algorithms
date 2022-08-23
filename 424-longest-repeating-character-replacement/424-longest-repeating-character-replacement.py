class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            freq[c] = 1 + freq.get(c, 0)
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            else:
                res = max(r - l + 1, res)
        return res