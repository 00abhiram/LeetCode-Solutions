class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ""
        nines = sum//9
        rem = sum % 9
        zeros = num - nines - (1 if rem > 0 else 0)
        result = "9" * nines
        if rem > 0:
            result += str(rem)
        result += "0" * zeros
        return result