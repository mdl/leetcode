def verticalTraversal(root):
  dic, minx, maxx = defaultdict(list), inf, -inf

  def dfs(node, x, y):
    nonlocal dic, minx, maxx
    minx, maxx = min(minx, x), max(maxx, x)
    dic[x].append((y, node.val))
    if node.left: dfs(node.left,  x - 1, y + 1)
    if node.right: dfs(node.right, x + 1, y + 1)

  dfs(root, 0, 0)

  out = []

  for x in range(minx, maxx + 1):
    out += [[val for y, val in sorted(dic[x])]]

  return out
