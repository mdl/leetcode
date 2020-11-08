  def inorder(root):
    result, stack, node = [], [], root

    while stack or node:
      while node:
        stack.append(node)
        node = node.left
    
      node = stack.pop()
      result.append(node.val)
      node = node.right

    return result
