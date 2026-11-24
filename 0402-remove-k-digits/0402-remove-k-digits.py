class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = list(map(int,num.strip()))
        st=[]
        for i in range(len(nums)):
            while st and k > 0 and nums[i] < st[-1]:
                st.pop()
                k -= 1
            st.append(nums[i])
        
        
        if k > 0:
            st = st[:-k]
        
        ans = ''.join(map(str, st)).lstrip('0')

        return ans if ans else '0'