class Solution:
    def maxRunTime(self, n, batteries):
        
        def can_run(time):
            total = 0
            for b in batteries:
                total += min(b, time)
            return total >= n * time
        
        left, right = 0, sum(batteries) // n
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_run(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans