class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l2 = [num for num in nums if num != 0]
        
        i = 0
        while i < len(l2):
            nums[i] = l2[i]
            i += 1
            
        i = len(l2)
        while i < len(nums):
            nums[i] = 0
            i += 1
            