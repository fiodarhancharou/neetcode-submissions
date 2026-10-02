class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find closest elem via binary search
        size = len(arr)
        l, r = 0, size - 1
        while r - l + 1 > k:
            mid = (l+r)//2
            if abs(arr[l]-x) > abs(arr[r]-x):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]
