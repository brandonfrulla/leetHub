class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cross = []
        if (len(nums1) > len(nums2)):
            for n in nums1:
                if n in nums2 and n not in cross:
                    cross.append(n)
        else:
            for n in nums2:
                if n in nums1 and n not in cross:
                    cross.append(n)
                    
        return cross