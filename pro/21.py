# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l2 is None:
            return l1
        if l1 is None:
            return l2

        if l1.val < l2.val:
            newNode = l1
            l1 = l1.next
        else:
            newNode = l2
            l2 = l2.next

        fakeHead = ListNode(-1)
        fakeHead.next = newNode
        while l1 and l2:
            if l1.val < l2.val:
                newNode.next = l1
                newNode = newNode.next
                l1 = l1.next
            else:
                newNode.next = l2
                newNode = newNode.next
                l2 = l2.next
        if l1:
            newNode.next = l1
        if l2:
            newNode.next = l2

        return fakeHead.next