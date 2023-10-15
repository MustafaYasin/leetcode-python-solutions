class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
    
        nums_set = set(nums)
        max_len = 0
        length = 0

        # for each number in the set, check if the number - 1 is in the set
        for num in nums_set:
            # if the number - 1 is not in the set, then we know that this is the start of a sequence
            if num - 1 not in nums_set:
                length = 1
                # check if the next number is in the set, if it is, then we know that the sequence continues
                while num + 1 in nums_set:
                    # if the next number is in the set, then we increment the length of the sequence
                    length += 1
                    # increment the number to check the next number in the sequence
                max_len = max(max_len, length)
        return max_len
