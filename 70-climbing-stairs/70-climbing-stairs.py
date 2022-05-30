class Solution:
    options = {0:0, 1:1, 2:2, 3:3}
    
    def climbStairs(self, n: int) -> int:
        return self.helper(n)
        
    def helper(self, n: int) -> int:
        if n in self.options:
            return self.options[n]
        else: 
            self.options[n] = self.helper(n-1) + self.helper(n-2)
            return self.options[n]