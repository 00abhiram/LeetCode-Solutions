class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) //2
            max_row = 0
            for r in range (1, m):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r
            left_is_greater = mid > 0 and mat[max_row][mid-1] > mat[max_row][mid]
            right_is_greater = mid < n - 1 and mat[max_row][mid + 1] > mat[max_row][mid]

            if not left_is_greater and not right_is_greater:
                return [max_row , mid]
            elif left_is_greater:
                high = mid - 1
            else:
                low = mid+1
        return[]