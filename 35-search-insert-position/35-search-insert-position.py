class Solution:
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        
        l = 0
        h = len(nums)
        
        while l < h:
            
            mid = (l + h) // 2
            
            if target > nums[mid]: 
                l = mid + 1
            else:
                h = mid
                
        return l
            