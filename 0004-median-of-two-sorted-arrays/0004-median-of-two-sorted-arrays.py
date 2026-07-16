class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #Brute force merge the arrays and sort
        '''merged = sorted(nums1+nums2)
        if len(merged)%2!=0:
            return merged[((len(merged)+1)/2)-1]
        else:
            return float(merged[(len(merged)/2)-1]+merged[(len(merged)/2)])/2'''
        
        '''#Two pointer 
        count = 0
        i = 0
        j = 0
        prev = 0
        curr = 0
        total_length = len(nums1)+len(nums2)
        median = (total_length)/2+1
        
        while count<(median):
            prev = curr
            if i == len(nums1):
                curr = nums2[j]
                j+=1
            elif j == len(nums2):
                curr = nums1[i]
                i+=1

            elif nums1[i]<nums2[j]:
                curr = nums1[i]
                i+=1
            else:
                curr = nums2[j]
                j+=1
            
            count+=1
        if total_length%2!=0:
            return curr
        else:
            return float(prev+curr)/2'''

        #Binary Search
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)

        lo = 0
        hi = m
        half = (m+n+1)/2

        while lo<=hi:
            i = (lo+hi)/2
            j = half - i

            l1 = nums1[i-1] if not (i==0) else float('-inf')
            r1 = nums1[i] if not (i==m) else float('inf')
            l2 = nums2[j-1] if not (j==0) else float('-inf')
            r2 = nums2[j] if not (j==n) else float('inf')
            

            if (l1<=r2 and l2<= r1) and (m+n)%2!=0:
                return max(l1,l2)
            
            elif (l1<=r2 and l2<= r1) and (m+n)%2==0:
                return (max(l1,l2)+min(r1,r2))/2.0
            
            elif l1>r2:
                hi = i-1
            else:
                lo = i+1
