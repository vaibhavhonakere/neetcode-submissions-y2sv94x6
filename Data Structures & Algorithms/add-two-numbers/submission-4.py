# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(not(l1)):
            return l2
        elif(not(l2)):
            return l1
        
        l1_node = l1
        l2_node = l2
        ret = ListNode(0)
        dummy = ret
        carry = 0

        while(l1_node and l2_node):
            first = l1_node.val
            second = l2_node.val
            output = first + second + carry
            num = (output) % 10 
            rem = (output) // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
            carry = rem
            l1_node = l1_node.next
            l2_node = l2_node.next
        
        while(l1_node):
            first = l1_node.val
            val = first + carry
            num = (val) % 10 
            rem = (val) // 10
            carry = rem
            dummy.next = ListNode(num)
            dummy = dummy.next
            l1_node = l1_node.next
        
        while(l2_node):
            second = l2_node.val
            val = second + carry
            num = (val) % 10 
            rem = (val) // 10
            carry = rem
            dummy.next = ListNode(num)
            dummy = dummy.next
            l2_node = l2_node.next
        
        if(carry):
            dummy.next = ListNode(carry)
            dummy = dummy.next    
        
        return ret.next

