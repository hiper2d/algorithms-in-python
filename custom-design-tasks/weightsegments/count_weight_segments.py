from typing import List


class Solution:

    @staticmethod
    def count_valid_segments(nums: List[int], k: int) -> int:
        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        counter = n

        for i in range(n):
            for j in range(i, n):
                if j == i:
                    memo[i][i] = (nums[i], nums[i])
                else:
                    prev_min, prev_max = memo[i][j-1]
                    new_val = nums[j]
                    if new_val > prev_max:
                        diff = new_val - prev_min
                        memo[i][j] = (prev_min, new_val)
                    elif new_val < prev_min:
                        diff = prev_max - new_val
                        memo[i][j] = (new_val, prev_max)
                    else:
                        diff = 0
                        memo[i][j] = memo[i][j-1]
                    if diff <= k:
                        counter += 1
        return counter
