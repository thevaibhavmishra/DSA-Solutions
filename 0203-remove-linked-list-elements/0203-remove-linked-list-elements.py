# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sh = ListNode(-1, head)
        prev = sh
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = prev.next
                head = head.next
        return sh.next