class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        cross = []
        if (len(s1) > len(s2)):
            for n in s2:
                if n in s1 and n not in cross:
                    cross.append(n)
        else:
            for n in s1:
                if n in s2 and n not in cross:
                    cross.append(n)
                    
        return cross