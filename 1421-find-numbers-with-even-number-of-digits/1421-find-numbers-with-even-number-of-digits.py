class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            digits = int(log10(n)) + 1
            if digits % 2 ==0:
                res += 1
        return res