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
        copy_map = {None: None}
        copy = head
        copy_1 = head
        while(head):
            copy_map[head] = Node(head.val)
            head = head.next
        
        while(copy):
            copy_map[copy].next = copy_map[copy.next]
            copy_map[copy].random = copy_map[copy.random]
            copy = copy.next

        return copy_map[copy_1]