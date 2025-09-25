import networkx as nx
import matplotlib.pyplot as plt

#Hàm tạo đồ thị vô hướng
def create_graph_by_nodes_and_edge(nodes, edges):
    # 1. Khởi tạo một đối tượng đồ thị
    # Sử dụng nx.Graph() để tạo đồ thị vô hướng
    G = nx.Graph()

    # 2. Thêm các đỉnh vào đồ thị
    G.add_nodes_from(nodes)

    # 3. Thêm các cạnh vào đồ thị
    G.add_edges_from(edges)
    return G

#Hàm tạo đồ thị có hướng
def create_digraph_by_nodes_and_edge(nodes, edges):
    # 1. Khởi tạo một đối tượng đồ thị
    # Sử dụng nx.DiGraph() để tạo đồ thị có hướng
    G = nx.DiGraph()

    # 2. Thêm các đỉnh vào đồ thị
    G.add_nodes_from(nodes)

    # 3. Thêm các cạnh vào đồ thị
    G.add_edges_from(edges)
    return G

#Hàm show đồ thị
def show_graph(graph, pos=None):
    # Nếu không có vị trí được cung cấp, sử dụng thuật toán bố cục ngẫu nhiên
    if pos is None:
        pos = nx.spring_layout(graph, seed=42)

    #Vẽ đồ thị
    nx.draw(graph, pos, with_labels=True)

    # Tắt trục tọa độ
    plt.axis('off')

    # Hiển thị đồ thị đã vẽ
    plt.show()

