class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

       
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc1, rc1, pre1, suf1, best1, len1 = a
            lc2, rc2, pre2, suf2, best2, len2 = b

            prefix = pre1
            if pre1 == len1 and rc1 == lc2:
                prefix = len1 + pre2

            suffix = suf2
            if suf2 == len2 and rc1 == lc2:
                suffix = len2 + suf1

            best = max(best1, best2)

            if rc1 == lc2:
                best = max(best, suf1 + pre2)

            return (
                lc1,
                rc2,
                prefix,
                suffix,
                best,
                len1 + len2
            )

        def build(node, left, right):
            if left == right:
                c = s[left]
                tree[node] = (c, c, 1, 1, 1, 1)
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, idx, char):
            if left == right:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (left + right) // 2

            if idx <= mid:
                update(node * 2, left, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, right, idx, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][4])

        return ans