class Solution:
    def minPathSum(self, nums: List[List[int]]) -> int:
        m,n=len(nums),len(nums[0])
        dp=[]
        for i in range(m):
            dp.append([float("inf")]*n)
        dp[0][0]=nums[0][0]
        for i in range(m):
            for j in range(n):
                for dx,dy in [(1,0),(0,1)]:
                    nx,ny=dx+i,dy+j
                    if 0<=nx<m and 0<=ny<n:
                        dp[nx][ny]=min(dp[nx][ny],nums[nx][ny]+dp[i][j])
        return dp[-1][-1]