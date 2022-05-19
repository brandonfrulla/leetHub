class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
    
        s, e = 0, len(nums)-1
        
        while s < e:
            tot = nums[s] + nums[e]
            
            if tot > t:
                e -= 1
            elif tot < t:
                s += 1
            else:
                return [s+1,e+1]