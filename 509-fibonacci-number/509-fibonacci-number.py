class Solution:
    vals = {0:0, 1:1}
    
    def fib(self, n: int ) -> int:
        
        if n in self.vals:
            return self.vals[n]
        
        self.vals[n] = self.fib(n-1) + self.fib(n-2)
        return self.vals[n]