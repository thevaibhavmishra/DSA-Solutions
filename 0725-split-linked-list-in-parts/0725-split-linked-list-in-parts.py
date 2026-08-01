# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def countList(head):
    c = 0
    while head:
        c+=1
        head = head.next
    return c
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        c = countList(head)
        r = c%k
        n = c//k
        res = []
        temp = head
        for i in range(k):
            e = 0 if r>0 else 1
            res.append(temp)
            for j in range(n - e):
                temp = temp.next
            if temp:
                tmp = temp.next
                temp.next = None
                temp = tmp
            r-=1
        return res
