# Problem Description:
# You are given the head of a linked list.

# Remove every node which has a node with a strictly greater value 
# anywhere to the right side of it.

# Return the head of the modified linked list.

# EXAMPLE:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodes(head):
    if not head:
        return 
    
    if not head.next:
        return head

    head.next = removeNodes(head.next)

    if head.next and head.val < head.next.val:
        return head.next

    return head