# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        '''s1 = ""
        s2 = ""
        temp = l1
        while temp!=None:
            s1+=str(temp.val)
            temp = temp.next
        temp = l2
        while temp!=None:
            s2+=str(temp.val)
            temp = temp.next
        num1 = int(s1[::-1])
        num2 = int(s2[::-1])
        res = str(num1+num2)
        
        l3 = ListNode(int(res[-1]),None)
        temp = l3
        for i in range(len(res)-2,-1,-1):
            new = ListNode(int(res[i]),None)
            temp.next = new
            temp = temp.next
        return l3'''

        dummy = ListNode(0)
        tail = dummy

        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total+=l1.val
                l1 = l1.next
            if l2:
                total+=l2.val
                l2 = l2.next
            digit = total%10
            carry = total//10
            tail.next = ListNode(digit,None)
            tail = tail.next

        return dummy.next
            