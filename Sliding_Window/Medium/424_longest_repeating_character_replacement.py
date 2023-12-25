class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left_pointer = 0
        maxf = 0
        res = 0

        # right_pointer is the end of the sliding window
        for right_pointer in range(len(s)):
            # count the frequency of each character
            count[s[right_pointer]] = 1 + count.get(s[right_pointer], 0)
            # update the max frequency
            maxf = max(maxf, count[s[right_pointer]])

            # if the number of characters that are not the most frequent is greater than k
            while (right_pointer - left_pointer + 1) - maxf > k:
                # move the left pointer to the right
                count[s[left_pointer]] -= 1
                # update the max frequency
                left_pointer += 1
            
            res = max(res, right_pointer - left_pointer + 1)

        return res

        