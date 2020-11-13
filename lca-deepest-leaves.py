def lcaDeepestLeaves(self, root):
  def dfs(node):
    if not node: return (-1, None)
    (hl, lcal) = dfs(node.left)
    (hr, lcar) = dfs(node.right)
    if hl > hr: return (hl + 1, lcal)
    if hr > hl: return (hr + 1, lcar)
    return (hr + 1, node)

  return dfs(root)[1]
