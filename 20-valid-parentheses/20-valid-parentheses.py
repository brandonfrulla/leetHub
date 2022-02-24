class Solution:
    
    def isValid(self, s: str) -> bool:
        
        stack=[]
        symbols = { ')' : '(', ']' : '[', '}' : '{' }
        
        #for each symbol in the string
        for sym in s:
            #print("symbol:", sym, "stack:", stack)
            
            if sym in symbols:
                top = stack.pop() if stack else '#'
                if symbols[sym] != top:
                    return False
                
            else:
                #print("appending:", sym)
                stack.append(sym)
                
        return not stack