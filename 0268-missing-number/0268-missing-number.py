class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i- nums[i]) # [0,1,2,3]-[0,1,3]
        return res

