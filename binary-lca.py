  def lca(root, p, q):
    ans = None
    
    # returns true if node subtree contains p or q
    def dfs(node):
      nonlocal ans
      if not node or ans: return False

      left, right = dfs(node.left), dfs(node.right)

      mid = node == p or node == q
      if mid + left + right >= 2: ans = node
      return mid or left or right
  
    dfs(root)

    return ans
