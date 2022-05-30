class Solution:
    options = {0:0, 1:1, 2:2, 3:3}
    
    def climbStairs(self, n: int) -> int:
        if n in self.options:
            return self.options[n]
        else: 
            self.options[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.options[n]