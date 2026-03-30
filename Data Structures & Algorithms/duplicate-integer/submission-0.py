class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for item in nums:
            freq[item] = 1+freq.get(item,0)
        
        count = 0

        for i in freq:
            if freq[i]>1:
                count+=1
        if count>=1:
            return True
        else:
            return False
        