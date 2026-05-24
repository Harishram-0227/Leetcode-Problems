# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0
        curr = head

        # Count total nodes
        while curr:
            curr = curr.next
            count += 1

        # Number of complete groups of size k
        iter = count // k

        if iter < 1:
            return None

        # Dummy node helps handle head reversal easily
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = end_node = head

        for _ in range(iter):

            # Move end_node to the node after current k-group
            for _ in range(k):
                end_node = end_node.next

            # Reverse current group using node pulling technique
            while curr.next != end_node:

                temp = curr.next

                # Remove temp from its position
                curr.next = temp.next

                # Insert temp at front of group
                temp.next = prev.next
                prev.next = temp

            # Move pointers for next group
            prev = curr
            curr = curr.next

        return dummy.next