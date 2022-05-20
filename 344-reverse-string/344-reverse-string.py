class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        _s,e = 0, len(s)-1
        
        while _s < e:
            temp = s[_s]
            s[_s] = s[e]
            s[e] = temp
            _s += 1
            e -= 1