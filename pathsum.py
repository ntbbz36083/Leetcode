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
			
#437. Path Sum III
#https://leetcode.com/problems/path-sum-iii/
##Recursive:
class Solution(object):
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target-root.val) + self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
##https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
##Iterative:
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        stack = [(root, [root.val])]
        num = 0
        
        while stack:
            node, totals = stack.pop()
            
            num += totals.count(sum)
                
            if node.left:
                stack.append((node.left, [x+node.left.val for x in totals]+[node.left.val]))
            if node.right:
                stack.append((node.right, [x+node.right.val for x in totals]+[node.right.val]))
        return num

#666. Path Sum IV
#https://leetcode.com/problems/path-sum-iv/
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.defaultdict(int)
        # Create a dict of depth and pos
        for num in nums:
            depth, pos = num/100, (num/10)%10
            val = num % 10
            # At each level, store the sum of all the previous nodes covered
            dic[depth, pos] = dic[depth-1, (pos+1)/2] + val
            
        res = 0
        for depth,pos in dic.keys():
            # Since the leaf nodes contain sum of the entire path from root to each leaf nodes, just check whether it is a leaf node or not and then add up all the leaf nodes
            if (depth+1, pos*2-1) not in dic and (depth+1,pos*2) not in dic:
                res += dic[depth,pos]
        return res	
