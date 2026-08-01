# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def revList(head):
    prev = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return head
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = revList(slow.next)
        slow.next = None
        while l2:
            tmp = l1.next
            l1.next = l2
            tmp2 = l2.next
            l2.next = tmp
            l1 = tmp
            l2 = tmp2
