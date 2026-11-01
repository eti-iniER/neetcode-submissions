# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head_a_nodes = {}
        head_b_nodes = {}
        head_a_obj = []
        head_b_obj = []

        count = 0
        while headA:
            n = id(headA)
            head_a_nodes[n] = count
            head_a_obj.append(headA)
            headA = headA.next
            count += 1
        
        count = 0
        while headB:
            n = id(headB)
            head_b_nodes[n] = count
            head_b_obj.append(headB)
            headB = headB.next
            count += 1
        
        best_id = None
        best = None

        for n in head_a_obj:
            if n in head_b_obj:
                return n
                # print(f"Intersection at {n.val}")
                # if best_id is not None and head_a_nodes[id(n)] < best_id:
                #     best_id = head_a_nodes[id(n)]
                #     best = n
        
        return best