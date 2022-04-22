class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif (nums[mid] < target):
                # cut off bottom half
                left = mid + 1 
            else:
                # cut off top half
                right = mid - 1
                 
        # it isn't there
        return -1