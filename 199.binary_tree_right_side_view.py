Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #iterative, time:O(n), space:O(n)

        if not root: return []
        res=[]
        q=collections.deque([(root,0)])
        while q:
        	node, lvl=q.popleft()
        	if lvl==len(res):
        		res.append(node.val)
        	if node.right:
        		q.append((node.right, lvl+1))
        	if node.left:
        		q.append((node.left, lvl+1))
        return res


        #recursive

        if not root: return []
        
        def helper(root, lvl):
        	if not root: return
        	if lvl==len(res):
        		res.append(root.val)
        	helper(root.right, lvl+1)
        	helper(root.left, lvl+1)

        res=[]
        helper(root,0)
        return res





