'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''1.建立一个头指针。2. 判断该位是否有数或者进位 3.将值赋值给临时变量。 4.将临时变量和进位相加，得到数值和进位'''
        head = ListNode(0)
        tmp = head
        carry = 0
        while(l1 or l2 or carry):
            newnode = ListNode(0)
            v1 = v2 = 0
            if(l1):
                v1 = l1.val
                l1 = l1.next
            if(l2):
                v2 = l2.val
                l2 = l2.next
            carry, newnode.val = divmod(v1+v2+carry,10)
            tmp.next = newnode
            tmp = newnode 
        return head.next
