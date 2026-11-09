class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def houserob(start, end):
            t = [-1] * (n + 1)

            def solve(i):
                if i > end:
                    return 0

                if t[i] != -1:
                    return t[i]

                t[i] = max(
                    nums[i] + solve(i + 2),
                    solve(i + 1)
                )

                return t[i]

            return solve(start)

        return max(houserob(0, n-2), houserob(1, n-1))