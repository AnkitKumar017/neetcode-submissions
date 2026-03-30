class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = len(nums1)-1
        j = 0

        while i>0 and j<len(nums2):
            if nums2[j]<nums1[i]:
                nums1[i],nums2[j] = nums2[j],nums1[i]
            i-=1
            j+=1
            
        nums1 = nums1 + nums2
        nums1.sort()

        l,r = 0,len(nums1)-1
        mid = (l+r)//2

        if len(nums1)%2==0:
            return (nums1[mid]+nums1[mid+1])/2
        else:
            return nums1[mid]

            
        