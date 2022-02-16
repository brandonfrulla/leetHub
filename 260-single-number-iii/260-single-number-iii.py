class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        found = []
        
        while len(found) != 2:
            for n in nums:
                if nums.count(n) == 1:
                    found.append(n)
                    
        return found