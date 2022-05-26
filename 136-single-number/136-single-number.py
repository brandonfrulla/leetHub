class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        trash = []
        for n in nums:
            if n not in trash:
                if nums.count(n) == 1:
                    return n
                else: 
                    trash.append(n)