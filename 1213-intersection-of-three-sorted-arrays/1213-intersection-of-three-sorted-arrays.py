class Solution:
    
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        #remove duplicates
        s1,s2,s3 = set(arr1), set(arr2), set(arr3)
        
        #get the xing of s1, with the xing of s2, with the xing of s1 and s3
        x = s1.intersection(s2.intersection(s3.intersection(s1)))
        
        #convert it to an array so it can be sorted
        l= []
        for _x in x:
            l.append(_x)
            
        l.sort()
        
        return l