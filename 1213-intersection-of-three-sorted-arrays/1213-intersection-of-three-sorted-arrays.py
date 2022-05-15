class Solution:
    def xing(self, s1, s2) -> List[int]:
        return [x for x in s1 if x in s2]
    
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        s1 = set(arr1)
        s2 = set(arr2)
        s3 = set(arr3)
        
        x1 = self.xing(s1, s2)
        x2 = self.xing(s1, s3)
        x3 = self.xing(s2, s3)
        
        x4 = self.xing(x1, x3)
        x5 = self.xing(x2, x3)
        
        x5.sort()
        
        return x5