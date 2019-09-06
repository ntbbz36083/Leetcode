Preorder:
**144. Binary Tree Preorder Traversal**
> Time Complexity O(N)
> Space Complexity O(1)
```
## Recursively
def preorderTraversal1(self, root):
    res = []
    self.dfs(root, res)
    return res
    
def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
		
## Iteratively
def preorderTraversal(self, root):
    def preorderTraversal(self, root):
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)    
                root = root.left     
            else:
                node = stack.pop()
                root = node.right
        return res
```
Inorder
**94. Binary Tree Inorder Traversal**
> Time Complexity O(N)
> Space Complexity O(1)
```

## Recursively
def inorderTraversal(self, root):
	res = []
	self.helper(root, res)
	return res

def helper(self, root, res):
	if root:
		self.helper(root.left, res)
		res.append(root.val)
		self.helper(root.right, res)

## Iteratively
def inorderTraversal(self, root):
    ans = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right   
    return ans
```
Preorder
**145. Binary Tree Postorder Traversal**
> Time Complexity O(N)
> Space Complexity O(1)
```
## Recursively
def postorderTraversal(self, root):
	self.res = []
	self.dfs(root)
	return self.res

def dfs(self, root):
	if not root:
		return 
	self.dfs(root.left)
	self.dfs(root.right) 
	self.res.append(root.val)
	
## Iteratively
def postorderTraversal(self, root):
	stack, res = [], []
	while stack or root:
		if root:
			stack.append(root)
			res.append(root.val)    
			root = root.right 
		else:
			node = stack.pop()
			root = node.left
	return res[::-1]
```
