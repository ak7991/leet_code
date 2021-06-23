from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        node = new_head = head
        temp = None
        prev_node = None
        pos = 1
        while node:
            if pos == left:
                rev_node = rev_node_init = ListNode(node.val)
                while node:
                    node = node.next
                    pos += 1
                    new_node = ListNode(node.val)
                    new_node.next = rev_node
                    rev_node = new_node
                    if pos == right:
                        break
                    a = []
                    temp = rev_node
                    while temp is not None:
                        a.append(temp.val)
                        temp = temp.next
                end_node = node.next
                rev_node_init.next = end_node
                if prev_node is not None:
                    prev_node.next = rev_node
                else:
                    new_head = rev_node
                break
            prev_node = node
            node = node.next
            pos += 1
        return new_head