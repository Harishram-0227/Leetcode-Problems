class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m == 0:
            return 1
        if n == 0:
            return 0

        dp = [[-1] * m for _ in range(n)]

        def dp_fn(i: int, j: int) -> int:
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = dp_fn(i - 1, j - 1) + dp_fn(i - 1, j)
            else:
                dp[i][j] = dp_fn(i - 1, j)
            return dp[i][j]

        return dp_fn(n - 1, m - 1)