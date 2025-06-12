class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l,r = 0,len(height)-1
        leftMax,rightMax = height[l],height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l] #subtracting height of cur pos(left) from max of left
            else:
                r -= 1
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r] #subtracting height of cur pos(right) from max of right
        return res



        