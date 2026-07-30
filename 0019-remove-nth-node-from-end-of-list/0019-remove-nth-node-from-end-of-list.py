# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def listLen(head):
    c = 0
    while head:
        c+=1
        head = head.next
    return c


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = listLen(head)
        n = c - n
        prev = ListNode(0, head)
        sh = prev
        for i in range(n):
            prev = head
            head = head.next
        prev.next = head.next
        return sh.next
