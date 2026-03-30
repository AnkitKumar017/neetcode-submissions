class Solution:
    def search(self, nums: List[int], target: int) -> int:

        freq = {}

        for num in nums:
            freq[num] = 1+freq.get(num,0)

        count = 0
        for i in freq:
            if i != target:
                count+=1
            else:
                return count

        return -1      