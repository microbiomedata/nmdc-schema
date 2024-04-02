import glob
import os

from ruamel.yaml import YAML
import networkx as nx
import matplotlib.pyplot as plt
from ruamel.yaml import YAML
import networkx as nx


def build_imports_graph(schema_dir):
    """
    Builds an imports graph from all YAML files under schema_dir.

    Args:
        schema_dir: Path to the directory containing YAML files.

    Returns:
        A networkx DiGraph representing the imports graph.
    """
    graph = nx.DiGraph()

    yaml = YAML(typ='safe')
    for filename in glob.iglob(f"{schema_dir}/*.yaml", recursive=False):
        # for filename in glob.iglob(f"{schema_dir}/**/*.yaml", recursive=True):
        with open(filename, 'r') as f:
            schema = yaml.load(f)
            if 'imports' in schema:
                for imported_schema in schema['imports']:
                    # Extract filename without extension and remove schema_dir prefix
                    node_name = os.path.splitext(os.path.basename(filename))[0].replace(f"{schema_dir}/", "")
                    imported_node_name = os.path.splitext(imported_schema)[0]
                    if "/" not in imported_node_name and \
                            imported_node_name != "mixs" and \
                            node_name != "mixs" and \
                            imported_node_name != "linkml:types" and \
                            node_name != "linkml:types":
                        graph.add_edge(node_name, imported_node_name)

    return graph


# Example Usage
schema_dir = "../schema"
graph = build_imports_graph(schema_dir)

# Simple visualization using networkx.draw
# Apply spring layout algorithm for uniform node placement
pos = nx.planar_layout(graph)  # Adjust parameters as needed

# Visualization using networkx.draw with node positions
plt.figure(figsize=(8, 6))
# nx.draw(graph, pos=pos, with_labels=True, font_weight='bold')
nx.draw(graph, pos=pos, with_labels=True, font_weight='bold', node_color='none')
# plt.show()

# plt.subplots_adjust(left=2, bottom=2, right=2, top=2)

plt.savefig("../../assets/partial-imports-graph.pdf", format="pdf", bbox_inches="tight")
plt.close()  # Optional: Close the plot window after saving

# circular_layout: Nodes arranged in a circle.
# shell_layout: Nodes arranged in concentric circles (useful for hierarchical structures).
# random_layout: Random node placement (may not be ideal for uniform distribution).
# spectral_layout: Uses spectral graph theory for node placement.
# kamada_kawai_layout: Force-directed layout for minimizing edge crossings.
# planar_layout: Tries to find a planar layout for planar graphs (no edge crossings).
