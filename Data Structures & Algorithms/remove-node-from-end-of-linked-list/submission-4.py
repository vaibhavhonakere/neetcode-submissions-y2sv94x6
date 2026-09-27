# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # move inital pointer

        ret = ListNode(0, head)
        dummy = ret

        while(n > 0):
            head = head.next
            n -= 1

        while(head):
            dummy = dummy.next
            head = head.next
        
        dummy.next = dummy.next.next

        return ret.next
