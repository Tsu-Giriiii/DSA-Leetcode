class Solution(object):
    def reverse(self, x):

        temp =x
        num = 0
        while abs(temp)>0:
            dig = abs(temp)%10
            temp = abs(temp)//10
            num = num*10+dig
        if len(str(format(num,'b')))>=32:
            return 0
        if x <0:
            return -num
        else:
            return num


        