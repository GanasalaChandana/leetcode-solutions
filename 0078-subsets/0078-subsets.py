class Solution:
    def subsets(self,nums):
        def backtrack(start,path):
            result.append(path[:]) #append copy of path snapshot
            for i in range(start,len(nums)):
                path.append(nums[i]) #include the nums[i] in the subset
                backtrack(i+1,path)  #continue to build subset from the next element
                path.pop() #exclude the nums[i] from the subset(backtrack)
        result = []
        backtrack(0,[])
        return result
        