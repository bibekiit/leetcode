'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
'''

# Solution 1: Two Pointers
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while pA != pB:
            # if pA is None, then pA = headB
            # if pB is None, then pB = headA
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
    
# Solution 2: Hash Table
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        pA = headA
        pB = headB
        while pA:
            visited.add(pA)
            pA = pA.next
        while pB:
            if pB in visited:
                return pB
            pB = pB.next
        return None
    
# Solution 3: Brute Force

# Time Complexity: O(n^2)

# Space Complexity: O(1)

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        pA = headA

        while pA:

            pB = headB

            while pB:

                if pA == pB:

                    return pA

                pB = pB.next

            pA = pA.next

        return None