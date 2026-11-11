class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        nxtgrt = []
        for i in range(len(nums2)-1,-1,-1):
            if not st:
                nxtgrt.append(-1)
                st.append(nums2[i])
            elif st[-1] <= nums2[i]:
                while st and st[-1] < nums2[i]:
                    st.pop()
                if not st:
                    nxtgrt.append(-1)
                    st.append(nums2[i])
                else:
                    nxtgrt.append(st[-1])
                    st.append(nums2[i])
            else:
                nxtgrt.append(st[-1])
                st.append(nums2[i])

        nxtgrt[:]= nxtgrt[::-1]
        res = []
        i = j = 0
        while i < len(nums1):

            if nums1[i] == nums2[j]:
                res.append(nxtgrt[j])
                i+=1
                j = 0
                continue

            j+=1
            if j >= len(nums2):
                j = 0
                i+= 1
        return res