class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        seen = set()

        def backtrack(temp):
            if len(temp) == n:
                result.append(temp[:])
                return 

            for i in range(n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    temp.append(nums[i])
                    backtrack(temp)
                    temp.pop()
                    seen.remove(nums[i])

        backtrack([])

        return result
