class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Initialize two pointers to start from the beginning and the end of the array in to save time
        l, r = 0, len(numbers) - 1

       # While the left pointer is less than the right pointer 
        while l < r:
            current_sum = numbers[l] + numbers[r]

            # If the current sum is alredy greater than the target, move the right pointer to the left
            if current_sum > target:
                r -= 1
            # If the current sum is less than the target, move the left pointer to the right
            elif current_sum < target:
                l += 1

            else: 
                return [l + 1, r + 1]     
        
        return []  

            
