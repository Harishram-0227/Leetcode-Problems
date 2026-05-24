class Solution:
    def maxSubArray(self, nums):

        maxSum = float('-inf')
        currSum = 0

        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0

        return maxSum