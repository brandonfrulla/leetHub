class Solution:
    def reverseWords(self, _st: str) -> str:
        
        ret = ""
        arr = _st.split()
        
        for w in arr:
            w = w[::-1]
            ret = ret + w+" "
        
        return ret.strip()