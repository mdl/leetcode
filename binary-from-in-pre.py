def buildTree(preorder, inorder):
  inorder_value_index_map = {val:idx for [idx, val] in enumerate(inorder)}
  curr_root_idx = 0

  def helper(left, right):
    nonlocal inorder_value_index_map, curr_root_idx
    if left == right: return None
    root_val = preorder[curr_root_idx]
    root = TreeNode(root_val)
    root_idx_inorder = inorder_value_index_map[root.val]
    curr_root_idx += 1
    root.left = helper(left, root_idx_inorder)
    root.right = helper(root_idx_inorder + 1, right)
    return root

  return helper(0, len(inorder))
