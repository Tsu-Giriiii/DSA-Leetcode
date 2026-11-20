class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        st = []
        ans = 0

        for i in range(n + 1):
            while st and (i == n or arr[st[-1]] >= arr[i]):
                mid = st.pop()

                left = st[-1] if st else -1
                right = i

                count = (mid - left) * (right - mid)
                ans += arr[mid] * count

            st.append(i)

        return ans % MOD

        