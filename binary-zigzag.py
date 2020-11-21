  def zigzag(root):
    if not root: return []

    res, temp, q, inorder = [], [], [root], 1

    while q:
      q1 = []

      for node in q:
        temp.append(node.val)
        if node.left: q1.append(node.left)
        if node.right: q1.append(node.right)
          
      res.append(temp[::inorder])
      temp = []
      inorder = inorder * -1
      q = q1

    return res
