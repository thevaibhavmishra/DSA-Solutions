# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mult(head):
    if not head: return 0
    c = mult(head.next)
    val = head.val*2 + c
    c = 1 if val > 9 else 0
    val = val%10
    head.val = val
    return c

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = mult(head)
        if c:
            head = ListNode(1, head)
        return head