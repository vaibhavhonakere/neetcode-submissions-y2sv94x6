# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def get_gcd(a,b):
            while(b > 0):
                a,b = b, a % b
            return a
        
        ret = ListNode(0, head)
        dummy = ret
        prev = head
        head = head.next
        while(head):
            # print(prev.val, head.val)
            cd = get_gcd(prev.val, head.val)
            node = ListNode(cd)
            dummy.next = ListNode(prev.val)
            dummy.next.next = ListNode(cd)
            dummy.next.next.next = ListNode(head.val)
            head = head.next
            prev = prev.next
            dummy = dummy.next.next


        return ret.next
