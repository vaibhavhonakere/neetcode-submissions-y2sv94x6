# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergedList(n1, n2):
            first = n1
            second = n2
            ret = ListNode(0)
            dummy = ret
            while(first and second):
                if(first.val < second.val):
                    dummy.next = first
                    first = first.next
                else:
                    dummy.next = second
                    second = second.next
                dummy = dummy.next
            
            if(first):
                dummy.next = first
                dummy = dummy.next
            
            if(second):
                dummy.next = second
                dummy = dummy.next

            return ret.next

        while(len(lists) > 1):
            merged_lists = []
            for i in range(0, len(lists), 2):
                node1 = lists[i]
                node2 = lists[i + 1] if i + 1 < len(lists) else None
                # print(node1, node2)
                merged = mergedList(node1, node2)
                merged_lists.append(merged)
            lists = merged_lists
        
        return lists[0] if lists else None



