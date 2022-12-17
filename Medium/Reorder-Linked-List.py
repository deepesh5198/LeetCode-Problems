# Problem Description:
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves 
# may be changed.

# EXAMPLE:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next


def reorderList(head):
    # check if none
    if head is None:
        return 

    # get the middle node in list
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # slow pointer will be the middle element
    
    # Now, reverse the second half of the list
    current = slow.next
    slow.next = None
    prev = None

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    # prev node will be the Head for second half
    # reveresed list

    # reordering the list
    current1 = head
    current2 = prev
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    return head

def reorderList_rec(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    prev_head = head
    
    def helper(head, prev_head):
        if head.next == None:
            return prev_head
        
        temp = helper(head.next, prev_head)
        
        if temp == None or temp.next == None or temp == head:
            return None

        back = temp.next
        temp.next = head.next
        head.next = None

        temp.next.next = back
        
        return temp.next.next
        
    helper(head, prev_head)


