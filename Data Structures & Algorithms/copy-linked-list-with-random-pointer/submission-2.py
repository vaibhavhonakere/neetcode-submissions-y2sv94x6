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
        oldToCopy = {None: None}
        curr = head
        while(curr):
            newNode = Node(curr.val)
            oldToCopy[curr] = newNode
            curr = curr.next
        
        curr = head
        while(curr):
            check = oldToCopy[curr]
            check.next = oldToCopy[curr.next]
            check.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]
