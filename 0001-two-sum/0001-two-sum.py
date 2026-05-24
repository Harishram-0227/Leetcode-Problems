class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums): #1
           rem = target - nums[i] #2
           
           if rem in seen: #3
               return [i, seen[rem]]  #4
           else:
               seen[value] = i  