# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def revList(head):
    curr = head
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        sh = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        rev = revList(slow.next)
        while rev:
            if rev.val != sh.val: return False
            print(rev.val, sh.val)
            rev, sh = rev.next, sh.next
        return True

        