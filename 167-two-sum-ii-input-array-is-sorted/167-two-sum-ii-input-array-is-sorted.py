class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         trash = []
        
#         for i in range(len(numbers)):
#             if numbers[i] not in trash:
#                 for j in range(i+1, len(numbers)):
#                     if numbers[i] + numbers[j] == target:
#                         return [i+1,j+1]
                
#             #nums[i] is not in the solution
#             trash.append(numbers[i])

        i = 0
        k = len(numbers) - 1
        
        while i < len(numbers) - 1:
            
            if numbers[i] + numbers[k] == target:
                return [i+1, k+1]
            elif numbers[i] + numbers[k] > target:
                k -= 1
            else:
                i += 1