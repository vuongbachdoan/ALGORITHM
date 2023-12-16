# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tempNode = head.next
        tempNode.next = None
        node = head
        while node.next != None:
            node = node.next
        node.next = tempNode
        return head.next