class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        n = len(asteroids)
        for i in range(n):
            while st and st[-1] > 0 and asteroids[i] < 0 and abs(asteroids[i])>abs(st[-1]):
                st.pop()
            if st and st[-1] > 0 and asteroids[i] < 0 and abs(asteroids[i])<=abs(st[-1]):
                if abs(asteroids[i])==abs(st[-1]):
                    st.pop()
                continue
            st.append(asteroids[i])
        return st
