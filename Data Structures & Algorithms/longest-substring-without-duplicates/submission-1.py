class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = 0
        res = 0
        seen = set()

        if not s:
            return 1

        for c in s:
            if c in seen:
                res = max(res,count)
                count = 1
            else:
                seen.add(c)
                count+=1

        return res

        