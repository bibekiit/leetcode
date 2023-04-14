# Given the head of a linked list, return the list after sorting it in ascending order.

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Example 1:

# Input: head = [4,2,1,3]

# Output: [1,2,3,4]

# Example 2:

# Input: head = [-1,5,3,4,0]

# Output: [-1,0,3,4,5]

# Example 3:

# Input: head = []

# Output: []

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].

# -105 <= Node.val <= 105

# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

# ListNode is not defined

class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next

class Solution:

    def sortList(self, head: ListNode) -> ListNode:

        if head is None:

            return None

        # find the middle of the list

        slow = head

        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next

            fast = fast.next.next

        # reverse the second half of the list

        prev = None

        curr = slow

        while curr is not None:

            next = curr.next

            curr.next = prev

            prev = curr

            curr = next

        # merge the two lists

        first = head

        second = prev

        while second.next is not None:

            first.next, first = second, first.next

            second.next, second = first, second.next

        return head
    

# I think this solution is wrong for sorting a list

# Path: medium/148. Sort List.py

# Compare this snippet from medium/143. Reorder List.py:

# You have a single linked list and you are trying to sort it

# You can only swap the nodes, not the values

# Example:

# Input: 4 -> 2 -> 1 -> 3

# Output: 1 -> 2 -> 3 -> 4

# Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next

class Solution:

    # maximum recursion depth exceeded
    def sortList(self, head: ListNode) -> ListNode:

        if head is None:

            return None
        
        if head.next is None:
                
            return head

        # find the middle of the list

        slow = head

        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next

            fast = fast.next.next

        # reverse the second half of the list

        prev = None

        curr = slow

        while curr is not None:

            next = curr.next

            curr.next = prev

            prev = curr

            curr = next

        # sort the two lists recursively and merge them

        first = self.sortList(head)

        second = self.sortList(prev)

        return self.merge(first, second)
    
    def merge(self, first, second):
        # merge the two lists
        dummy = ListNode()
        curr = dummy
        while first is not None and second is not None:
            if first.val < second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next
        if first is not None:
            curr.next = first
        if second is not None:
            curr.next = second
        return dummy.next
    