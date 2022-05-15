class Solution:
    
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        s1,s2,s3 = set(arr1), set(arr2), set(arr3)
        x = s1.intersection(s2.intersection(s3.intersection(s1)))
        
        l= []
        for _x in x:
            l.append(_x)
            
        l.sort()
        
        return l