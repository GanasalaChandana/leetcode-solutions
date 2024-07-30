class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset: #if there exists a duplicate
                return True
            hashset.add(n)
        return False
        
        