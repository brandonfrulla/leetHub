class Solution:
    def s_intersection(self, s1, s2) -> List[int]:
        return [n for n in s1 if n in s2]
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        if (len(s1) > len(s2)):
            return self.s_intersection(s2, s1)
        else:
            return self.s_intersection(s1, s2)