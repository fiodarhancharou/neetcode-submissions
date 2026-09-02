class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = [5, 10, 20]
        change = {i: 0 for i in notes}
        price = 5
        for bill in bills:
            change[bill] += 1
            diff = bill - price

            for note in notes[::-1]:
                while note <= diff and change[note]:
                    diff -= note
                    change[note] -= 1
            if diff:
                return False
        return True