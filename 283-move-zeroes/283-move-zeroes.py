class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #get all non-zeros
        l = [num for num in nums if num != 0]
        
        i = 0
        while i < len(nums):
            #push non-zeros to front
            if i < len(l):
                nums[i] = l[i]
            #everything else is 0
            else:
                nums[i] = 0
            i += 1
            
            