# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot :
            return True
        
        if not root :
            return False
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
    
    def sameTree(self,t1,t2):
        queue = deque([(t1,t2)])
        while queue:
            n1,n2 = queue.pop()
            if not n1 and not n2 :
                continue
            if not n1 or not n2 :
                return False
            
            if n1.val != n2.val :
                return False
            queue.append((n1.left,n2.left))
            queue.append((n1.right,n2.right))
        return True
