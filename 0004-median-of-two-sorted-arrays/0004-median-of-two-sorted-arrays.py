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
        
        #Two pointer 
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
            return float(prev+curr)/2