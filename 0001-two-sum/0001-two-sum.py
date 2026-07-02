class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''#Brute Force
        #Create 3 variables num1=0 and num2=1, positons = []
        num1 = 0
        num2 =1
        positions = []
        #while num2< len(nums)
        while num1 < len(nums)-1:
            while num2 < len(nums):
                if (nums[num1]+nums[num2])== target:
                    positions.append(num1)
                    positions.append(num2)
                    return positions
                else:
                    num2+= 1
            num1 +=1
            num2 = num1+1  ''' 
        
        num=0
        positions = {}
        for i in range(len(nums)):
            positions[nums[i]] = i
        while num < len(nums):
            if (target-nums[num]) in positions and positions[target-nums[num]]!=num:
                return [num,positions[target-nums[num]]]
            num +=1

