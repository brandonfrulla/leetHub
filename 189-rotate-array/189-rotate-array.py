class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k = k % len(nums) 
        
        s1 = nums[len(nums)-k::1]
        s2 = nums[0:len(nums)-k:]
        
        i = 0
        while i < len(s1):
            nums[i] = s1[i]
            i +=1
            
        i = 0
        while i < len(s2):
            nums[len(s1)+i] = s2[i]
            i += 1