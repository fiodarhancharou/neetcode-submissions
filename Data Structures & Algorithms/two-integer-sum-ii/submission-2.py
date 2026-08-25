class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        holder = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if num in holder:
                return [holder[num] + 1, i+1]
            else:
                holder[diff] = i

            