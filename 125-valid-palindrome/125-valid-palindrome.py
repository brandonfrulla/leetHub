class Solution:
    def clean(self, s: str) -> str:
        s = s.lower()
        letters = list(string.ascii_lowercase)
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        
        for _s in s:
            if (_s not in letters) and (_s not in numbers):
                s = s.replace(_s,'')
                
        return s
    
    def isPalindrome(self, s: str) -> bool:
        
        s = self.clean(s)
        rev = s[::-1]
        
        
        return rev == s