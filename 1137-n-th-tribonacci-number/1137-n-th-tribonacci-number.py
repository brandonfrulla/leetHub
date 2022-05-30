class Solution:
    vals = {0:0, 1:1,2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.vals:
            return self.vals[n]
        elif n < 0:
            return 0
        else:
            self.vals[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
            return self.vals[n]