import bisect

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        
        land_end = sorted(s + d for s, d in zip(landStartTime, landDuration))
        water_end = sorted(s + d for s, d in zip(waterStartTime, waterDuration))
        
        ans = float('inf')
        
        # Case 1: Land first → Water second
        # finish = max(waterStart[j], landEnd[i]) + waterDuration[j]
        for j in range(len(waterStartTime)):
            ws, wd = waterStartTime[j], waterDuration[j]
            
            # Find split: how many land rides end <= ws
            idx = bisect.bisect_right(land_end, ws)
            
            if idx > 0:
                # Some land ride ends before water opens → tourist waits at water
                # finish = ws + wd  (same for all such land rides, just need one)
                ans = min(ans, ws + wd)
            
            if idx < len(land_end):
                # Some land ride ends AFTER water opens → use smallest such landEnd
                # finish = land_end[idx] + wd  (idx is smallest end > ws)
                ans = min(ans, land_end[idx] + wd)
        
        # Case 2: Water first → Land second
        # finish = max(landStart[i], waterEnd[j]) + landDuration[i]
        for i in range(len(landStartTime)):
            ls, ld = landStartTime[i], landDuration[i]
            
            # Find split: how many water rides end <= ls
            idx = bisect.bisect_right(water_end, ls)
            
            if idx > 0:
                # Some water ride ends before land opens → tourist waits at land
                ans = min(ans, ls + ld)
            
            if idx < len(water_end):
                # Some water ride ends AFTER land opens → use smallest such waterEnd
                ans = min(ans, water_end[idx] + ld)
        
        return ans