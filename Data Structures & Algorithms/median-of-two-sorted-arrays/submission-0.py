class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        length = len(nums1)+len(nums2)
        nums1 = nums1 + [0]*(length-1)

        l = len(nums1)-1
        right = 0

        while l >= 0 r < len(nums2):
            if nums2[r]>=nums1[l]:
                nums1 = nums1=nums2
        """

        nums1 = sorted(nums1+nums2)
            
        l,r = 0,len(nums1)-1

        mid = (l+r)//2

        if len(nums1)%2 == 0:
            res = (nums1[mid]+nums1[mid+1])/2
        else:
            res = nums1[mid]

        return (res)
        