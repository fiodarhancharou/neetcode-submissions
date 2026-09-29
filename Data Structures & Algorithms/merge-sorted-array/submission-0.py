class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p2, p3 = 0, 0
        min_len = min(m, n)
        stack = []
        nums3 = nums1[:m+1]
        i = 0
        while p2 < n and p3 < m:
            if nums2[p2] < nums3[p3]:
                nums1[i] = nums2[p2]
                p2 += 1
            elif nums2[p2] > nums3[p3]:
                nums1[i] = nums3[p3] 
                p3 += 1
            else:
                nums1[i] = nums2[p2]
                i += 1
                p2 += 1
                nums1[i] = nums3[p3]
                p3 += 1
            i += 1
        if p2 == n:
            for j in range(p3,m):
                nums1[i] = nums3[j]
                i += 1
        if p3 == m:
            for j in range(p2,n):
                nums1[i] = nums2[j]
                i += 1
