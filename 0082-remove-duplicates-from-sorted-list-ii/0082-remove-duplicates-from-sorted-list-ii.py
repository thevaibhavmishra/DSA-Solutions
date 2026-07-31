# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        sh = ListNode(-1, head)
        prev = sh
        curr = head
        while curr:
            if curr.next and curr.next.val == curr.val:
                v = curr.val
                while curr and curr.val == v:
                    curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        return sh.next