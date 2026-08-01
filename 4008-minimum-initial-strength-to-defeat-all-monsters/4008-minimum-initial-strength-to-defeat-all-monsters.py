class Solution(object):
    def minInitialStrength(self, monsters, boosts):
        """
        :type monsters: List[int]
        :type boosts: List[List[int]]
        :rtype: int
        """
        n = len(monsters)

        # Calculate bonus at every index using difference array
        diff = [0] * (n + 1)

        for l, r, v in boosts:
            diff[l] += v
            diff[r + 1] -= v

        bonuses = [0] * n
        bonus = 0

        for i in range(n):
            bonus += diff[i]
            bonuses[i] = bonus

        # Check whether a given initial strength is enough
        def can_defeat(initial):
            strength = initial

            for i in range(n):
                if strength + bonuses[i] < monsters[i]:
                    return False

                strength -= monsters[i]

                if strength < 0:
                    strength = 0

            return True

        lo = 0
        hi = sum(monsters)

        while lo < hi:
            mid = (lo + hi) // 2

            if can_defeat(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo