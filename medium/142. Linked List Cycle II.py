# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?

# Example 1:

# Input: head = [3,2,0,-4], pos = 1

# Output: tail connects to node index 1

# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:

# Input: head = [1,2], pos = 0

# Output: tail connects to node index 0

# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:

# Input: head = [1], pos = -1

# Output: no cycle

# Explanation: There is no cycle in the linked list.

# Constraints:

# The number of the nodes in the list is in the range [0, 104].

# -105 <= Node.val <= 105

# pos is -1 or a valid index in the linked-list.

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

    def detectCycle(self, head: ListNode) -> ListNode:

        if head is None:

            return None

        slow = head

        fast = head

        # find the meeting point

        # slow moves 1 step at a time

        # fast moves 2 steps at a time

        # if there is a cycle, they will meet at some point

        # if there is no cycle, fast will reach the end

        # and we can return None


        while fast is not None and fast.next is not None:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:

                break

        # no cycle
        if fast is None or fast.next is None:

            return None

        # there is a cycle

        # reset slow to head

        # move slow and fast 1 step at a time

        # they will meet at the start of the cycle

        # return the meeting point


        slow = head

        while slow != fast:

            slow = slow.next

            fast = fast.next

        return slow
    