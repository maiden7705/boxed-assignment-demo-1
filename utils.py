# Imports
import os
import graphviz

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

def distinct_depth_nodes(d, root):
  for a, b in d.items():
      if isinstance(b, dict):
        edges.append((root, a))
        distinct_depth_nodes(b, a)

def foo():
    a = 1 + 1