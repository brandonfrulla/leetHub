class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, h = 0, len(nums)-1
        
        if target < nums[l]:
            return 0
        elif target > nums[h]:
            return len(nums)
        else:
            
            while l <= h:
                m = (l + h) // 2
                
                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    l = m + 1
                else:
                    h = m - 1
                    
            return l