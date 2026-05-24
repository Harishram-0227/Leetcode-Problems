# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge_sort(head):
            # Base Case: 0 or 1 node
            if not head or not head.next:
                return head

            # Optimization: Handle 2 nodes explicitly to reduce recursion overhead
            if not head.next.next:
                if head.val < head.next.val:
                    return head
                else:
                    first, second = head, head.next
                    second.next = first
                    first.next = None
                    return second
            
            # Find the middle using slow/fast pointers
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # Split the list into two halves
            mid = slow.next
            slow.next = None
            
            # Recursively sort both halves
            left_side = merge_sort(head)
            right_side = merge_sort(mid)

            # Merge the two sorted lists
            if left_side.val <= right_side.val:
                current = left_side
                p1, p2 = left_side.next, right_side
            else:
                current = right_side
                p1, p2 = left_side, right_side.next
            
            new_head = current
            
            while p1 or p2:
                if not p1:
                    current.next = p2
                    break
                elif not p2:
                    current.next = p1
                    break
                
                if p1.val <= p2.val:
                    current.next = p1
                    p1 = p1.next
                else:
                    current.next = p2
                    p2 = p2.next
                current = current.next
                
            return new_head
        
        return merge_sort(head)

