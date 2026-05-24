class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        def f(day,buy,count):
            if day==n or count==0:
                return 0
            if dp[day][buy][count]!=-1:
                return dp[day][buy][count]
            if buy:
                profit=max(-prices[day]+f(day+1,0,count),f(day+1,1,count))
            else:
                profit=max(prices[day]+f(day+1,1,count-1),f(day+1,0,count))
            dp[day][buy][count]=profit
            return dp[day][buy][count]
        return f(0,1,2)