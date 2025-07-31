class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted((nums))
        d={}
        for i,num in enumerate(temp):
            if num not in d:
                d[num] = i
        res = []
        for i in nums:
            res.append(d[i])  # d = {1:0,2:1,3:2,8:4}
        return res
