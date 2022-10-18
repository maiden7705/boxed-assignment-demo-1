import json, os, graphviz
from graphviz import Source
from IPython.display import Image
# variables
edges = []

# dummy changes

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
        keys(item, 'event')
    edges_deduped = removeDuplicates(edges)
    # print(edges_deduped)

    # Dump edges in a grapgViz format
    digraphStr = 'strict digraph tree {\n'
    for row in edges_deduped:
        digraphStr = digraphStr + '    {0} -> {1};\n'.format(*row)
    digraphStr = digraphStr + '}'
    print(digraphStr)
    graph_img_filePath = os.path.join(os.getcwd(), 'Requirement/json_tree.gv')
    with open(graph_img_filePath, "w") as text_file:
        text_file.write(digraphStr)

    Source.from_file(graph_img_filePath, format='png').save()
    Image(filename=graph_img_filePath+'.png')