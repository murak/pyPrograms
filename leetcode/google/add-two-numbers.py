# Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        res = l3 = ListNode(-1) #sentinal node
        carry = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            l3.next = ListNode(sum % 10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            sum = carry + l1.val
            carry = sum // 10
            l3.next = ListNode(sum % 10)
            l1 = l1.next
            l3 = l3.next
        
        while l2 is not None:
            sum = carry + l2.val
            carry = sum // 10
            l3.next = ListNode(sum % 10)
            l2 = l2.next
            l3 = l3.next
        
        if carry > 0:
            l3.next = ListNode(carry)
        
        return res.next
