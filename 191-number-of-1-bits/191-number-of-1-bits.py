class Solution:
    def hammingWeight(self, n: int) -> int:
        
        v = str(bin(n))
        a = [str(m) for m in v]
        return a.count("1")
        
        