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

#Hàm lấy bậc của đỉnh
def get_node_degree(graph, node):
    """
    Trả về bậc của một đỉnh trong đồ thị.
    Hàm tự động phân biệt đồ thị vô hướng và có hướng.

    Args:
        graph (nx.Graph or nx.DiGraph): Đồ thị.
        node: Đỉnh cần kiểm tra.

    Returns:
        int or dict: Bậc của đỉnh (đối với đồ thị vô hướng) 
                     hoặc dictionary chứa bán bậc vào/ra (đối với đồ thị có hướng).
    
    Raises:
        ValueError: Nếu đỉnh không tồn tại trong đồ thị.
    """
    if not graph.has_node(node):
        raise ValueError(f"Lỗi: Đỉnh '{node}' không tồn tại trong đồ thị.")

    if isinstance(graph, nx.DiGraph):
        return {
            'in_degree': graph.in_degree(node),
            'out_degree': graph.out_degree(node)
        }
    else:
        return graph.degree(node)
    
#Hàm lấy đỉnh liền kề
def get_node_neighbors(graph, node):
    """
    Trả về danh sách các đỉnh liền kề với một đỉnh cụ thể trong đồ thị.
    Hàm này hoạt động với cả đồ thị vô hướng và đồ thị có hướng.

    Args:
        graph (nx.Graph or nx.DiGraph): Đồ thị.
        node: Đỉnh cần tìm các đỉnh liền kề.

    Returns:
        list: Một danh sách chứa các đỉnh liền kề.

    Raises:
        ValueError: Nếu đỉnh không tồn tại trong đồ thị.
    """
    if not graph.has_node(node):
        raise ValueError(f"Lỗi: Đỉnh '{node}' không tồn tại trong đồ thị.")

    return list(graph.neighbors(node))    

#Hàm lấy thông tin đỉnh
def get_node_info(graph, node):
    """
    Trả về một dictionary chứa thông tin chi tiết (bậc và các đỉnh kề)
    của một đỉnh trong đồ thị.
    
    Args:
        graph (nx.Graph or nx.DiGraph): Đồ thị.
        node: Đỉnh cần lấy thông tin.

    Returns:
        dict: Một dictionary chứa thông tin chi tiết của đỉnh.
              - Đối với đồ thị vô hướng: 'degree' và 'neighbors'.
              - Đối với đồ thị có hướng: 'in_degree', 'out_degree' và 'neighbors'.

    Raises:
        ValueError: Nếu đỉnh không tồn tại trong đồ thị.
    """
    if not graph.has_node(node):
        raise ValueError(f"Lỗi: Đỉnh '{node}' không tồn tại trong đồ thị.")
        
    info = {}
    
    # Lấy thông tin bậc
    if isinstance(graph, nx.DiGraph):
        info['in_degree'] = graph.in_degree(node)
        info['out_degree'] = graph.out_degree(node)
    else:
        info['degree'] = graph.degree(node)
        
    # Lấy danh sách các đỉnh liền kề
    info['neighbors'] = list(graph.neighbors(node))
    
    return info

#Hàm kiểm tra liên thông của đồ thị vô hướng
def check_undirected_connectivity(graph):
    """
    Kiểm tra trạng thái liên thông của một đồ thị vô hướng.

    Args:
        graph (nx.Graph): Đồ thị vô hướng cần kiểm tra.

    Returns:
        str: "Đồ thị liên thông" nếu đồ thị liên thông, ngược lại là "Đồ thị không liên thông".
    """
    if nx.is_connected(graph):
        return "Đồ thị liên thông."
    else:
        return "Đồ thị không liên thông."
    
def check_directed_connectivity(graph):
    """
    Kiểm tra trạng thái liên thông của một đồ thị có hướng.

    Args:
        graph (nx.DiGraph): Đồ thị có hướng cần kiểm tra.

    Returns:
        str: Trạng thái liên thông mạnh, yếu, hoặc không liên thông.
    """
    if nx.is_strongly_connected(graph):
        return "Đồ thị liên thông mạnh."
    elif nx.is_weakly_connected(graph):
        return "Đồ thị liên thông yếu."
    else:
        return "Đồ thị không liên thông."




