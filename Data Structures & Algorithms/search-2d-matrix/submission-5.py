class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary(arr,target):
            l,r = 0,len(arr)-1

            while l<=r:
                mid = (l+r)//2

                if arr[mid]<target:
                    l = mid+1
                elif arr[mid]>target:
                    r = mid-1
                else:
                    return 1
            return 0
        
        ans = 0
        for i in range(len(matrix)):
            ans = binary(matrix[i],target)
            if ans==1:
                return True
        
        return False
        