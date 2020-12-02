def lowestCommonAncestor(self, p, q):
  # set of numbers - values of visited parent nodes
  visited = set()
  stack = [p, q]

  while stack:
    node = stack.pop()
    if node.val in visited: return node
    visited.add(node.val)
    if node.parent: stack.append(node.parent)

  return None
