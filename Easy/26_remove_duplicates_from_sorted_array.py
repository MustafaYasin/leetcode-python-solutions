class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # intialize left pointer
        left_pointer = 1

        # iterate through nums while right pointer scans the array to find next unique elements   
        for right_pointer in range(1, len(nums)):
            if nums[right_pointer] != nums[right_pointer - 1]:
                nums[left_pointer] = nums[right_pointer]

                # increment left pointer, right pointer is incremented by for loop
                left_pointer += 1
        
        # return left pointer as it is the length of the array with unique elements
        return left_pointer



