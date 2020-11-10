  def deleteNode(root, key):
    if not root: return None
    if key < root.val: root.left = deleteNode(root.left, key)
    elif root.val < key: root.right = deleteNode(root.right, key)
    else:
      if not root.right: return root.left
      if not root.left: return root.right           
      node = root.right
      mini = node.val
      while node.left:
        node = node.left
        mini = node.val
      root.val = mini
      root.right = deleteNode(root.right, root.val)
    return root
