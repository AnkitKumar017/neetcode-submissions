class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = 1+freq.get(num,0)  

        for i in freq:
            if freq[i]>1:
                return i     