# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cursor = dummy
        nodes_to_reverse = right - left + 1

        while left - 1 > 0:
            cursor = cursor.next
            head = head.next
            left -= 1

        prev = None
        for _ in range(nodes_to_reverse):
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        cursor.next.next = head
        cursor.next = prev

        return dummy.next