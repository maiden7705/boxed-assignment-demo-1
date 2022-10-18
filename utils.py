# Imports
import os

# variables
distinct_elements = []
node_tree_list = []
distinct_flat_node_tree_list = []
flat_list = []
edges = []

def get_last_elements(node):
  if (len(node.split(':')) > 1):
    return node.rsplit(':', 2)[-2]
  return ''

def keys(d, c = []):
  return [i for a, b in d.items() for i in ([c+[a]] if not isinstance(b, dict) else keys(b, c+[a]))]

def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]

def flatten_nested_list(lst):
  return [item for sublist in lst for item in sublist]

def item_in_this_list(item, lst):
  last_match = 0
  nodeLst = item.split(':')
  if len(nodeLst) == 1:
    return None
  for i, node in enumerate(nodeLst):
    if node in lst:
      last_match = i
      continue;
    return nodeLst[last_match] if last_match == 0 else ':'.join(nodeLst[0:last_match + 1])

def distinct_list_elements(lst):
  for node in lst:
    if node not in distinct_flat_node_tree_list:
        distinct_flat_node_tree_list.append(node)

def create_diagraph_file(edges_deduped):
    digraphStr = 'strict digraph tree {\n'
    for row in edges_deduped:
        digraphStr = digraphStr + '    {0} -> {1};\n'.format(*row)
    digraphStr = digraphStr + '}'
    print(digraphStr)
    # graph_img_filePath = os.path.join(os.getcwd(), 'json_tree.gv')
    with open('json_tree.gv', "w") as text_file:
        text_file.write(digraphStr)

def distinct_depth_nodes(d: dict, root: str):
  for a, b in d.items():
      if isinstance(b, dict):
        edges.append((root, a))
        distinct_depth_nodes(b, a)

def foo():
    a = 1 + 1