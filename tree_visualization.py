import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def dfs(node):
    stack = [(node, 0)]
    result = []
    while stack:
        node, level = stack.pop()
        if node:
            result.append(node)
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))
    return result


def bfs(node):
    queue = [(node, 0)]
    result = []
    while queue:
        node, level = queue.pop(0)
        if node:
            result.append(node)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    return result


def generate_colors(n):
    colors = []
    for i in range(n):
        shade = int(255 * (i + 1) / n)
        colors.append(f"#{shade:02x}{shade:02x}00")
    return colors


def visualize_tree(root, traversal_sequence):
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    graph = add_edges(graph, root, pos)

    colors = generate_colors(len(traversal_sequence))
    color_map = {}
    for i, node in enumerate(traversal_sequence):
        color_map[node.id] = colors[i]
        node.color = colors[i]  # Оновлюємо колір вузла

    node_colors = [color_map[node] for node in graph.nodes]

    plt.figure(figsize=(12, 8))
    nx.draw(
        graph,
        pos,
        labels=nx.get_node_attributes(graph, "label"),
        node_color=node_colors,
        with_labels=True,
        node_size=1500,
        font_size=10,
        font_color="white",
    )
    plt.show()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

dfs_sequence = dfs(root)
bfs_sequence = bfs(root)

visualize_tree(root, dfs_sequence)
visualize_tree(root, bfs_sequence)
