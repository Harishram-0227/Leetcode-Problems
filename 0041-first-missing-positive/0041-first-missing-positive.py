class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # index placement
        n=len(nums)
        i=0
        while i<n:
            correct_ord=nums[i]-1 #placing value in its index position
            if 1<=nums[i]<=n and nums[i]!=nums[correct_ord]: #first condition checks whether current number is useful, because -ve or 0 or num>n are useless and 2nd condition prevents infinite swapping 
                nums[i],nums[correct_ord]=nums[correct_ord],nums[i] #swapping is done over here
            else:
                i+=1 #if 1st condition fails then i moves by 1 and either one of -ve or 0 or >n num is present at that position
        for i in range(n):
            if nums[i]!=i+1: #checks the first missing +ve
                return i+1 #return the element as i is the gap(index) and i+1 is the value that needs to be placed at that index
        return n+1 #if every element is correctly indexed without any gaps        