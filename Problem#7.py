# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.


### This Code is Only For Vs Code.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    dummy = ListNode()
    tail = dummy
    for num in arr:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

def linked_list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next


l1 = array_to_linked_list([1, 2, 4])
l2 = array_to_linked_list([1, 3, 4])

merged = mergeTwoLists(l1, l2)
print(linked_list_to_array(merged))



### This is Code is LeetCode Solution code

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next