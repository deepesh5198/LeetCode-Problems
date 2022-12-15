# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def swapPairs(head):
    if not head:
        return head
    
    prev = None
    current = head
    ans = head.next

    while current and current.next:
        adj = current.next

        if prev: 
            prev.next = adj

        current.next, adj.next = adj.next, current

        prev, current = current, current.next


    return ans or head

# RECURSIVE SOLUTION
def swapPairs(head):
    if not head:
        return

    if not head.next:
        return head

    current = head.next
    
    temp = current.next
    current.next = head
    head.next = temp
    # current.next, head.next = head, current.next

    head.next = swapPairs(head.next)

    return current
    