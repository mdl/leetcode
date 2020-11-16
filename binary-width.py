  def widthOfBinaryTree(root):
    width, left, right = 0, {}, {}
    
    def dfs(node, num = 0, dep = 0):
      nonlocal width
      if node:
        if not dep in left: left[dep] = num
        right[dep] = max(right[dep] if dep in right else 0, num)
        width = max(width, right[dep] - left[dep] + 1)
        dfs(node.left, 2 * num, dep + 1)
        dfs(node.right, 2 * num + 1, dep + 1)
      
    dfs(root)    

    return width
