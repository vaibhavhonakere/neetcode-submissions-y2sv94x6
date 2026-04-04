/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ArrayList<ListNode> mergedList = new ArrayList<>();
        for(int i=0; i < lists.length; i++){
            mergedList.add(lists[i]);
        }
        if(mergedList.size() == 0){
            return null;
        }
        while(mergedList.size() > 1){
            ArrayList<ListNode> tmp = new ArrayList<>();
            for(int i=0; i < mergedList.size(); i = i+2){
                ListNode first = mergedList.get(i);
                ListNode second = null;
                if(i + 1 < mergedList.size()){
                    second = mergedList.get(i + 1);
                }
                tmp.add(mergeL(first, second));
            }
            mergedList = tmp;
            System.out.println(mergedList);
        }
        return mergedList.get(0);

    }
    private ListNode mergeL(ListNode first, ListNode second){
        ListNode ret_1 = new ListNode(0);
        ListNode ret = ret_1;
        while(first != null && second != null){
            if(first.val < second.val){
                ret.next = first;
                first = first.next;
            }else{
                ret.next = second;
                second = second.next;
            }
            ret = ret.next;
        }
        if(first != null){
            ret.next = first;
            first = first.next;
        }
        if(second != null){
            ret.next = second;
            second = second.next;
        }
        return ret_1.next;

    }
}
