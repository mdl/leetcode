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

def lowestCommonAncestorZeroSpace(self, p, q):
  p1, p2 = p, q
  while p1 != p2:
    p1 = p1.parent if p1.parent else q
    p2 = p2.parent if p2.parent else p

  return p1
