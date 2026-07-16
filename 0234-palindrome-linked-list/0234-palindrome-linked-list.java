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
    public ListNode reverselist(ListNode head){

            ListNode prev = null;
            ListNode curr = head;

            while(curr != null){
                ListNode next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
            }
            return prev;
        }

        public ListNode middle(ListNode head){
            ListNode hare = head;
            ListNode turtle = head;

            while(hare.next != null && hare.next.next != null){
                turtle = turtle.next;
                hare = hare.next.next;
            }
            return turtle;
        }


    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next== null){
            return true;
        }

        ListNode middlenode = middle(head);
        ListNode Secoundhalf = reverselist(middlenode.next);

        ListNode Firsthalf = head;
            while(Secoundhalf != null){
            if(Firsthalf.val != Secoundhalf.val){
                return false;
            }
            Firsthalf = Firsthalf.next;
            Secoundhalf = Secoundhalf.next;
        }
        return true;
        
    }
}