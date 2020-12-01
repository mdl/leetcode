  def longestConsecutive(root):
    ans = 0
    
    def dfs(node):
      nonlocal ans
      if not node: return (inf, 0, 0)
      (lval, linc, ldec), (rval, rinc, rdec) = dfs(node.left), dfs(node.right)

      val = node.val
      inc = max(linc + 1 if val - 1 == lval else 1, rinc + 1 if val - 1 == rval else 1)
      dec = max(ldec + 1 if val + 1 == lval else 1, rdec + 1 if val + 1 == rval else 1)
      ans = max(ans, inc + dec - 1)
      
      return (val, inc, dec)
    
    dfs(root)
    
    return ans
