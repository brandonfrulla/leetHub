class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        return self.helper(left, right, nums, target)
    
    def helper(self, left:int, right:int, nums: List[int], target: int) -> int:
        
        if left>right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif (nums[mid] < target):
            # cut off bottom half
            return self.helper(mid+1, right, nums, target)
        else:
            # cut off top half
            return self.helper(left, mid-1, nums, target)
                 
        # it isn't there    
        return -1