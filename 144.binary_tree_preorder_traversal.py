144.binary_tree_preorder_traversal.py

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #recursion, time:O(n) space:O(n), worst case, call stack
#         if not root: return []
#         def dfs(root):
#             if not root:
#                 return
#             res.append(root.val)
#             dfs(root.left)
#             dfs(root.right)
            
#         res=[]
#         dfs(root)
#         return res

		#iterative time:O(n) space:O(n)
        if not root: return []
        st=[root]
        res=[]
        while st:
            node=st.pop()
            res.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return res