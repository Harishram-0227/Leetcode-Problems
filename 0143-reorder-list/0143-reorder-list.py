class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # -----------------------------
        # Step 1: Find middle
        # -----------------------------
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # -----------------------------
        # Step 2: Reverse second half
        # -----------------------------
        prev = None
        temp = slow.next

        # split the list
        slow.next = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        # -----------------------------
        # Step 3: Merge both halves
        # -----------------------------
        first = head
        second = prev

        while second:

            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2