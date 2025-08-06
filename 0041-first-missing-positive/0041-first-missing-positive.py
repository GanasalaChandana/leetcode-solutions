class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Replace negative numbers and zeros with 0s (or any placeholder > n)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 0
        
        # Step 2: Mark presence using index
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (n + 1)
        
        # Step 3: First index with positive number means missing positive integer
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        
        # Step 4: If all positions are marked correctly
        return n + 1
