# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def revFun(head):
    if not head or not head.next: return head
    prev = None
    nex = None
    while head:
        nex = head.next
        head.next = prev
        prev = head
        head = nex
    return prev
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #l1 = revFun(l1)
        #l2 = revFun(l2)
        ans = ListNode()
        tmp = ans
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            carry = 1 if s > 9 else 0
            ans.next = ListNode(s%10)
            ans = ans.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            ans.next = ListNode(1)
        return tmp.next
