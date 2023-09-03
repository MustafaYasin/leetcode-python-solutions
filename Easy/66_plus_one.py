class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # reverse the array to start from the end
        digits = digits[::-1]
        
        # initialize carry and set first digit to 1
        one, i = 1, 0

        # iterate through the array while there is a carry
        while one:

            # if the index is within the array, add the carry to the digit
            if i < len(digits):
                digits[i] += one
                # if the digit is 10, set it to 0 and carry 1
                digits[i] = 0
            # if the index is out of the array, append the carry to the array
            else:
                digits.append(one)
                one = 0
            
            i += 1
        # reverse the array back to the original order
        return digits[::-1]