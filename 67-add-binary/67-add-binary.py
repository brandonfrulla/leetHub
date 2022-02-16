class Solution:
        
    def decimalToBinary(self, n, l):
        num = l
        if(n > 1):
            self.decimalToBinary(n//2, num)
        num.append(n%2)
        return num
    
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        
        c = a+b
        num = []        
        final = self.decimalToBinary(c, num)
        
        return ''.join(str(n) for n in final)