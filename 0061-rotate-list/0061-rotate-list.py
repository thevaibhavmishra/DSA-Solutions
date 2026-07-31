# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def listLength(head):
    c = 0
    last = None
    while head:
        c+=1
        last = head
        head = head.next
    return c, last


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c, last = listLength(head)
        if not c or not k%c: return head
        n = c - k%c
        curr = head
        for i in range(n-1):
            curr = curr.next
        res = curr.next
        curr.next = None
        last.next = head
        return res