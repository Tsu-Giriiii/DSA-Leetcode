class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for a,b in invocations:
            graph[a].append(b)

        visited= set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for next in graph[node]:
                dfs(next)
        dfs(k)
        
        ans = []
        for a,b in invocations:
            if a not in visited and b in visited:
                for i in range(n):
                    ans.append(i)
                return ans
        
        for i in range(n):
            if i not in visited:
                ans.append(i)
        return ans

        