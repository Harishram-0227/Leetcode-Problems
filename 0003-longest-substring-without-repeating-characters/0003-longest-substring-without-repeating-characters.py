class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            # If s[r] not in seen, we can keep increasing the window size
            if s[r] not in seen:
                output = max(output, r - l + 1)
            else:
                # There are two cases if s[r] in seen:
                # case1: s[r] is inside the current window
                # case2: s[r] is not inside the current window
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            
            seen[s[r]] = r
        return output
