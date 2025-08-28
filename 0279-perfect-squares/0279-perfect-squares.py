class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0

        for target in range(1,n+1):
            for s in range(1,target+1):  #going through every number's square
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target],1 + dp[target-square])  #bottom up approach
        
        return dp[n]


        #Time complexity is O(n*n^1/2)