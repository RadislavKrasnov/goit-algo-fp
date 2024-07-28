import uuid
import heapq
import colorsys
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    nx.draw_networkx_labels(tree, pos=pos, labels=labels, font_color='white')
    plt.show()

def build_min_heap(array):
    heapq.heapify(array)
    length = len(array)
    nodes = [Node(key) for key in array]
    for i in range(length):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < length:
            nodes[i].left = nodes[left_index]
        
        if right_index < length:
            nodes[i].right = nodes[right_index]
    
    return nodes[0]

def generate_colors(n):
    start_h, start_s, start_v = 240 / 360, 1, 0.2 # Темно-синій в HSV
    end_h, end_s, end_v = 240 / 360, 0.5, 1 # Світло-синій в HSV
    return [colorsys.hsv_to_rgb(
        start_h,
        start_s + i * (end_s - start_s) / (n - 1),
        start_v + i * (end_v - start_v) / (n - 1)
    ) for i in range(n)]

def bfs(root, colors_qty):
    if root is None:
        return
    
    colors = generate_colors(colors_qty)
    queue = deque([root])

    while len(queue) > 0:
        current = queue.popleft()
        current.color = colors.pop(0)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

data = [0, 4, 5, 10, 1, 3]
heap_root = build_min_heap(data)
bfs(heap_root, len(data))
draw_tree(heap_root)
