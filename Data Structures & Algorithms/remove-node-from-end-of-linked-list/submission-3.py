# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ret = ListNode(0, head)
        dummy = ret

        fast = head
        while(n > 0):
            fast = fast.next
            n -= 1
        
        while(fast):
            dummy = dummy.next
            fast = fast.next
        
        dummy.next = dummy.next.next
        return ret.next
            