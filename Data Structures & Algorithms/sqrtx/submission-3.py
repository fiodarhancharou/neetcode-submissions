class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        if x < 2:
            return x
        while l < r:
            mid = (l+r) // 2
            quad = mid ** 2
            if quad == x:
                return mid
            elif quad < x:
                l = mid + 1
            elif quad > x:
                r = mid
        if quad > x:
            return mid - 1
        return mid