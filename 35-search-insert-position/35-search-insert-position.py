class Solution:
    def helper(self, _nums: List[int], _target: int, _l: int, _h: int) -> int:
        while _l <= _h:
            _m = (_l + _h) // 2
                
            if _nums[_m] == _target:
                return _m
            elif _target > _nums[_m]:
                _l = _m + 1
            else:
                _h = _m - 1
                
        return _l
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        
        if target < nums[l]:
            return 0
        elif target > nums[h]:
            return len(nums)
        else:
            return self.helper(nums, target, l, h)
            