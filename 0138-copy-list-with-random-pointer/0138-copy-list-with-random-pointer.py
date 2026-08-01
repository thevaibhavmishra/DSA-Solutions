"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        listNodes = {}
        temp = head
        res = Node(0)
        curr = res
        while temp:
            newNode = Node(temp.val)
            listNodes[temp] = newNode
            curr.next = newNode
            temp = temp.next
            curr = curr.next
        temp1 = head
        temp2 = res.next
        while temp1:
            if temp1.random:
                temp2.random = listNodes[temp1.random]
            temp1 = temp1.next
            temp2 = temp2.next
        return res.next
        
        