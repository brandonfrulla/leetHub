class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        s, e = 0, len(nums)-1
        ans = [0] * len(nums)
        
        i = e
        while i >= 0:
            
            if abs(nums[s]) > abs(nums[e]):
                #print(nums[s]**2)
                ans[i] = nums[s]**2
                s += 1
            else:
                #print(nums[e]**2)
                ans[i] = nums[e]**2
                e -= 1
            #print(ans)
            i -= 1
            
        return ans