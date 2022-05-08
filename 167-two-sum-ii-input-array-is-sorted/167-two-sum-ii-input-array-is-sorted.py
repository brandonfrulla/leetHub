class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        i = 0
        k = len(numbers) - 1
        
        while i < len(numbers) - 1:
            if numbers[i] + numbers[k] == target:
                return [i+1, k+1]
            elif numbers[i] + numbers[k] > target:
                k -= 1               
            else:
                i += 1