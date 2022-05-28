class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        _n = set(nums)
        
        n = len(nums) + 1
        for num in range(n):
            if num not in _n:
                return num