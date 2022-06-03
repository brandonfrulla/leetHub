class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = ""
        for i in digits:
            num = num + str(i)
            
        _num = int(num)
        
        retVal = str(_num + 1)
        return [i for i in str(retVal)]
            
            