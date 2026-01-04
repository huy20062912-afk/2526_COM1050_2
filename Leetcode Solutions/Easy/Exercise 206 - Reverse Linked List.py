# Exercise 206: Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Making 2 nodes:
        prev = None 
        curr = head
        while curr:
            next_temp = curr.next # Saving the next node
            curr.next = prev # Reversing the direction of node arrow
            # Make the nodes step 1 step ahead
            prev = curr
            curr = next_temp
        # When Curr is None, prev will be in the final node (the head of the new linked list)
        return prev
        