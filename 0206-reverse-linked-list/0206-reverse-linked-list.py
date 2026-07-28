# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def revfun(head):
    if not head or not head.next: return head, head
    smallHead, tail = revfun(head.next)
    tail.next = head
    head.next = None
    return smallHead, head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return revfun(head)[0]