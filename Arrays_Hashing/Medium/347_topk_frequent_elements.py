class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # initialize a dictionary to store the count of each number
        count = {}
        
        # initialize a list of lists to store the numbers with their frequency as the index
        freq = [[] for _ in range(len(nums) + 1)]

        # iterate through the list and store the count of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # iterate through the dictionary and store the numbers in a list with their frequency as the index
        for n, c in count.items():
            freq[c].append(n)

        ans = []

        # iterate through the list of lists in reverse order and check the numbers with the highest frequency
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
                


