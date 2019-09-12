#112. Path Sum
#https://leetcode.com/problems/path-sum/
##Iterative:
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, sum)]
        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right and node.val == val:
                    return True
                stack.append((node.right, val - node.val))
                stack.append((node.left, val - node.val))
        return False
##Recursive		
class Solution(object):
    # DFS Recursively 
    def hasPathSum(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        return any(res)

    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right and root.val == target:
                res.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)
				
#113. Path Sum II
#https://leetcode.com/problems/path-sum-ii/
##Iterative:
class Solution(object):
    def pathSum(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, sum, [])]
        while stack:
            curr, val, ls = stack.pop()
            if curr:
                if not curr.left and not curr.right and curr.val == val:
                    res.append(ls + [curr.val])                
                stack.append((curr.right, val-curr.val, ls+[curr.val]))
                stack.append((curr.left, val-curr.val, ls+[curr.val]))
        return res 

##Recursive:
def pathSum1(self, root, sum):
    res = []
    self.dfs(root, sum, [], res)
    return res
    
def dfs(self, root, sum, path, res):
    if root:
        if sum == root.val and not root.left and not root.right:
            res.append(path+[root.val])
        self.dfs(root.left, sum-root.val, path+[root.val], res)
        self.dfs(root.right, sum-root.val, path+[root.val], res)
			
	
