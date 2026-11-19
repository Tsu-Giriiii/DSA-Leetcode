class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        st = []
        temp = []
        prev = [0]
        n = len(nums)
        while prev!=temp:
            prev[:] = temp
            for i in range(n-1,-1,-1):
                
                while st and st[-1] <= nums[i]:
                    st.pop()
                if len(temp)<n:
                    if st:
                        temp.append(st[-1])
                    else:
                        temp.append(-1)
                else:
                    if st:
                        temp[i] = st[-1]
                    else:
                        temp[i] = -1
                st.append(nums[i])
                
            if prev == temp:
                break
        
        return temp