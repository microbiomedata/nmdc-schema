import glob
import os
from ruamel.yaml import YAML
import networkx as nx
import plotly.graph_objects as go


def build_imports_graph(schema_dir):
    graph = nx.DiGraph()
    yaml = YAML(typ='safe')
    for filename in glob.iglob(f"{schema_dir}/*.yaml", recursive=False):
        with open(filename, 'r') as f:
            schema = yaml.load(f)
            if 'imports' in schema:
                for imported_schema in schema['imports']:
                    node_name = os.path.splitext(os.path.basename(filename))[0].replace(f"{schema_dir}/", "")
                    imported_node_name = os.path.splitext(imported_schema)[0]
                    graph.add_edge(node_name, imported_node_name)
    # Find all simple cycles in the graph
    cycles = list(nx.simple_cycles(graph))
    if cycles:
        print("Cycles detected:")
        for cycle in cycles:
            print(cycle)
    else:
        print("No cycles found.")

    return graph


def find_redundant_paths(graph):
    redundant_paths = []
    for node in graph.nodes():
        for successor in graph.nodes():
            if node != successor:
                # Check if there is a direct edge from `node` to `successor`
                if graph.has_edge(node, successor):
                    # Now, check if there's also an indirect path
                    try:
                        paths = list(nx.all_simple_paths(graph, source=node, target=successor))
                        if len(paths) > 1:
                            # More than one path indicates a redundant path
                            redundant_paths.append((node, successor, paths))
                    except nx.NetworkXNoPath:
                        pass
    return redundant_paths


def visualize_imports_graph(graph):
    pos = nx.arf_layout(graph)
    # pos = nx.spring_layout(graph, seed=42)

    edge_x = []
    edge_y = []
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = []
    node_y = []
    node_labels = []
    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_labels.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='Viridis',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2
        ),
        text=node_labels,
        textposition='top center'
    )

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(graph.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append(f'{node_labels[node]}')

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    fig = go.Figure(data=[node_trace],
                    layout=go.Layout(
                        title='Schema Imports Graph',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    # Add edges as arrows
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        fig.add_annotation(
            x=x1, y=y1,
            ax=x0, ay=y0,
            xref='x', yref='y',
            axref='x', ayref='y',
            showarrow=True,
            arrowhead=1,  # Arrowhead style
            arrowsize=2.5,  # Arrowhead size
            arrowwidth=1,  # Arrow stem width
            arrowcolor='#888'  # Arrow color
        )

    fig.show()


# Example usage
schema_dir = "../../schema"
graph = build_imports_graph(schema_dir)

redundant_paths = find_redundant_paths(graph)
if redundant_paths:
    print("Redundant paths found:")
    for path in redundant_paths:
        print(f"{path[0]} directly and indirectly imports {path[1]}")
else:
    print("No redundant paths found.")

visualize_imports_graph(graph)
