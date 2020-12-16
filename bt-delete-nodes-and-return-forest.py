  def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    if not root: return []
    
    forest = []
    toDelete = set(to_delete)

    def dfs(node, parent, d):
      nonlocal forest, toDelete
      if not node: return
      val = node.val
      
      if not parent and not (val in toDelete):
        forest.append(node)
      
      if val in toDelete:
        if parent:
          if d == 'l': parent.left = None
          else: parent.right = None
        dfs(node.left, None, 'l')
        dfs(node.right, None, 'r')
      else:
        dfs(node.left, node, 'l')
        dfs(node.right, node, 'r')
         
    dfs(root, None, None)
    
    return forest
