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

# Solution 1: Merge Sort

# Time Complexity: O(nlogn)

# Space Complexity: O(1)
class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next

class Solution:

    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:

            return head

        # find the middle node

        slow = fast = head

        while fast.next and fast.next.next:

            slow = slow.next

            fast = fast.next.next

        # split the list into two parts

        mid = slow.next

        slow.next = None

        # sort each part

        left = self.sortList(head)

        right = self.sortList(mid)

        # merge two parts

        return self.merge(left, right)
    
    def merge(self, left, right):
            
            dummy = ListNode(0)
    
            curr = dummy
    
            while left and right:
    
                if left.val < right.val:
    
                    curr.next = left
    
                    left = left.next
    
                else:
    
                    curr.next = right
    
                    right = right.next
    
                curr = curr.next
    
            if left:
    
                curr.next = left
    
            if right:
    
                curr.next = right
    
            return dummy.next