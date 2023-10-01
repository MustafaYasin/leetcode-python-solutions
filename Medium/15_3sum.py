class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        l, r = 1, len(nums) - 1
    
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
           
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesome = v + nums[l] + nums[r]

                if threesome > 0:
                    r -=  1

                elif threesome < 0:
                    l += 1

                else:
                    result.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return result


        
        