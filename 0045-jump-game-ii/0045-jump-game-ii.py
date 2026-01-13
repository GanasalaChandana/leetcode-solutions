class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,i + nums[i])
            l = r + 1
            r = farthest #where u can jump
            res += 1 #how many jumps we are taking to get to that endpoint
        return res