  def constructFromPrePost(preorder, postorder):
    def dfs(pre, post):
      if not pre: return None
      if len(pre) == 1: return TreeNode(pre[0])
      
      root = pre[0]
      rootNode = TreeNode(root)
      leftRoot = pre[1]
      rightRoot = post[-2]
      
      if leftRoot == rightRoot:
        rootNode.left = dfs(pre[1:], post[:-1])
        return rootNode

      predivider = pre.index(rightRoot)
      postdivider = predivider - 2
      preleft, preright = pre[1:predivider], pre[predivider:]
      postleft, postright = post[:postdivider + 1], post[postdivider + 1:-1]
      rootNode.left = dfs(preleft, postleft)
      rootNode.right = dfs(preright, postright)
      return rootNode
      
    return dfs(preorder, postorder)
