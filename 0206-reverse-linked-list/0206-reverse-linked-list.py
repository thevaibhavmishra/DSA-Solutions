# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def revfun(head):
    if not head or not head.next: return head
    smallHead = revfun(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return revfun(head)