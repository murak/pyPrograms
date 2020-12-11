# Leet code problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        d = sentinal = ListNode(0)
        carry = 0
        while p != None or q != None:
            carry = carry // 10
            if p != None:
                carry += p.val
                p = p.next
            
            if q != None:
                carry += q.val
                q = q.next
            
            d.next = ListNode(carry % 10)
            d = d.next
            
        if carry // 10 > 0:
            d.next = ListNode(carry // 10)
        
        return sentinal.next
            