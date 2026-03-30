class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0

        while l<len(nums):
            for i in range(l+1,len(nums)):
                if target-nums[l]==nums[i]:
                    return [l,i]
            l+=1
        
        