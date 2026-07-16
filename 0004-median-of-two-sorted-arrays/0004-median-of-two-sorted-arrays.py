class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #Brute force merge the arrays and sort
        merged = sorted(nums1+nums2)
        if len(merged)%2!=0:
            return merged[((len(merged)+1)/2)-1]
        else:
            return float(merged[(len(merged)/2)-1]+merged[(len(merged)/2)])/2
        #Two pointer 
        '''count = 0
        i = 0
        j = 0
        median = (len(nums1)+len(nums2)+1)/2
        total_length = len(nums1)+len(nums2)

        if len(nums1)==0:
            return nums2[median-1]
        elif len(nums2)==0:
            return nums1[median-1]
        
        while count<(median-1):
            if nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
            
            count+=1
        if total_length%2!=0:
            return min(nums1[i],nums2[j])
        else:
            return float((nums1[i]+nums2[j]))/2'''