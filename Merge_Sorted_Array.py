class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
        
        left = m - 1
        right = m + n - 1
        right2 = n - 1
        
        while left >= 0 and right2 >= 0:
            if nums2[right2] >= nums1[left]:
                nums1[right] = nums2[right2]
                right2 -= 1
                right -= 1
            else:
                nums1[right] = nums1[left]
                left -= 1
                right -= 1
            
        if right2 >= 0:
            while right2 >= 0:
                nums1[right2] = nums2[right2]
                right2 -= 1
            
