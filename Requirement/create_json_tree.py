import json, os
# variables
edges = []

def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]

def keys(d, root):
  # [i for a, b in d.items() for i in (edges.append((root, a)) if not isinstance(b, dict) else keys(b, a))]
  for a, b in d.items():
      if isinstance(b, dict):
        edges.append((root, a))
        keys(b, a)
    
if __name__ == "__main__":
    currDir = os.path.dirname(__file__)
    with open(os.path.join(currDir, './testEventData-1.json'), 'r') as f:
        events_json = json.load(f)

    for item in events_json['events']:
        keys(item, 'events')
    edges_deduped = removeDuplicates(edges)
    # print(edges_deduped)

    # Dump edges in a grapgViz format
    print('strict digraph tree {')
    for row in edges_deduped:
        print('    {0} -> {1};'.format(*row))
    print('}')