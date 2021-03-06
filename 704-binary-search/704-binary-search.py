class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(0, len(nums)-1, nums, target)
    
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