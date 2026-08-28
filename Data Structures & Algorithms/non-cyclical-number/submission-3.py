class Solution:
    def isHappy(self, n: int) -> bool:
        holder = set()
        square = n
        while square != 1:
            
            digits = [int(i)**2 for i in str(square)]
            square = sum(digits)
            print(holder, square)

            if square in holder:
                return False
            holder.add(square)
        return True