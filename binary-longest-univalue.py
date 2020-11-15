  def longestUnivaluePath(root):
    ans = 0
    
    # returns longest path WHICH INCLUDES node
    # and which could be reused by upper nodes
    # and updates answer
    def dfs(node):
      nonlocal ans
      if not node: return 0
      left, right = dfs(node.left), dfs(node.right)
      
      selfleft, selfright = 0, 0
      if node.left and node.left.val == node.val:
        selfleft = left + 1
      if node.right and node.right.val == node.val:
        selfright = right + 1
      
      ans = max(ans, selfleft + selfright)
      return max(selfleft, selfright)
      
    dfs(root)
    
    return ans
