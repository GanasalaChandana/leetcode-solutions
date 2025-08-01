class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            print('num:', i)
            xor ^= i
            print('xor:', xor)
        return xor