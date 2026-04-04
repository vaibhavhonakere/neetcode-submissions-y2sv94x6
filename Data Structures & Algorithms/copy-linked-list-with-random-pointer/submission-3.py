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
        copy = {None: None}
        tmp = head
        while(tmp):
            copy[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        print(copy)
        
        tmp2 = head
        while(tmp2):
            copy[tmp2].random = copy[tmp2.random]
            copy[tmp2].next = copy[tmp2.next]
            tmp2 = tmp2.next
        
        return copy[head]

