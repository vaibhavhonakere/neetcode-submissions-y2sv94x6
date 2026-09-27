# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1) DO the slow and fast pointer to find the middle,
        # and then after that we have both halves. 

        # 2) We reverse the second half

        # 3) Alternate the first and reversed second half nodes, and 
        # return the dummy node


        slow = head
        fast = head.next

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list 
        prev = None
        second_half = slow.next
        slow.next = None
        while(second_half):
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        
        # Alternate

        first = head
        second = prev

        while(first and second):
            tmp_1 = first.next
            tmp_2 = second.next
            first.next = second
            second.next = tmp_1
            first = tmp_1
            second = tmp_2

        # first.next = None
