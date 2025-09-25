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
    
#Hàm tạo ma trận kề cho đồ thị vô hướng    
def create_adj_matrix_undirected(graph, nodes):
    """
    Hàm tạo ma trận kề cho đồ thị vô hướng.

    Args:
        graph: Đồ thị.
        nodes: Danh sách các đỉnh trong đồ thị.

    Returns:
        list: Một ma trận kề dưới dạng danh sách các danh sách (list of lists).

    Raises:
        ValueError: Nếu một đỉnh trong graph.edges() không tồn tại trong danh sách nodes.
    """
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]

    # Tạo một từ điển để ánh xạ đỉnh sang chỉ số, giúp tìm kiếm hiệu quả hơn
    node_to_index = {node: i for i, node in enumerate(nodes)}

    for u_node, v_node in graph.edges():
        try:
            u_index = node_to_index[u_node]
            v_index = node_to_index[v_node]
        except KeyError:
            # Raise ValueError nếu đỉnh không tồn tại
            raise ValueError(f"Đỉnh '{u_node}' hoặc '{v_node}' không tồn tại trong danh sách nodes.")

        # Đặt 1 cho cả hai chiều vì đây là đồ thị vô hướng
        adj_matrix[u_index][v_index] = 1
        adj_matrix[v_index][u_index] = 1

    return adj_matrix

#Hàm tạo ma trận kề cho đồ thị có hướng
def create_adj_matrix_directed(graph, nodes):
    """
    Tạo ma trận kề cho một đồ thị có hướng.

    Args:
        graph: Đối tượng đồ thị có hướng.
        nodes: Danh sách các đỉnh trong đồ thị.

    Returns:
        list: Ma trận kề dưới dạng danh sách các danh sách.

    Raises:
        ValueError: Nếu một đỉnh trong graph.edges() không tồn tại trong danh sách nodes.
    """
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]

    # Tạo một từ điển để ánh xạ đỉnh sang chỉ số, giúp tìm kiếm hiệu quả hơn
    node_to_index = {node: i for i, node in enumerate(nodes)}

    # Duyệt qua các cạnh và chỉ thêm một chiều
    for u_node, v_node in graph.edges():
        try:
            u_index = node_to_index[u_node]
            v_index = node_to_index[v_node]
        except KeyError:
            # Raise ValueError nếu đỉnh không tồn tại
            raise ValueError(f"Đỉnh '{u_node}' hoặc '{v_node}' không tồn tại trong danh sách nodes.")

        # Thêm cạnh từ u_node đến v_node
        adj_matrix[u_index][v_index] = 1

    return adj_matrix

#Hàm in ma trận kề
def print_adj_matrix(adj_matrix, nodes):
    """
    In ma trận kề một cách rõ ràng và dễ đọc.

    Args:
        adj_matrix (list): Ma trận kề dưới dạng danh sách các danh sách.
        nodes (list): Danh sách các đỉnh tương ứng với ma trận kề.
    """
    if not adj_matrix or not nodes:
        print("Ma trận kề hoặc danh sách đỉnh rỗng.")
        return

    # Tạo hàng tiêu đề cột
    header = "   " + " ".join([str(node) for node in nodes])
    print(header)

    # In từng hàng của ma trận
    for i, row in enumerate(adj_matrix):
        # In tiêu đề hàng (đỉnh) và các giá trị của hàng đó
        row_str = " ".join(map(str, row))
        print(f"{nodes[i]}| {row_str}")
   
#Hàm tạo danh sách kề cho đồ thị vô hướng        
def create_adj_list_undirected(graph, nodes):
    """
    Tạo danh sách kề cho đồ thị vô hướng.

    Args:
        graph: Đối tượng đồ thị.
        nodes: Danh sách các đỉnh trong đồ thị.

    Returns:
        dict: Một từ điển biểu diễn danh sách kề.

    Raises:
        ValueError: Nếu một đỉnh trong graph.edges() không tồn tại trong danh sách nodes.
    """
    adj_list = {node: [] for node in nodes}

    for u_node, v_node in graph.edges():
        if u_node not in adj_list or v_node not in adj_list:
            raise ValueError(f"Đỉnh '{u_node}' hoặc '{v_node}' không tồn tại trong danh sách nodes.")

        # Thêm các đỉnh liền kề vào danh sách của nhau.
        adj_list[u_node].append(v_node)
        adj_list[v_node].append(u_node)

    return adj_list

#Hàm tạo danh sách kề cho đồ thị có hướng
def create_adj_list_directed(graph, nodes):
    """
    Tạo danh sách kề cho đồ thị có hướng.

    Args:
        graph: Đối tượng đồ thị.
        nodes: Danh sách các đỉnh trong đồ thị.

    Returns:
        dict: Một từ điển biểu diễn danh sách kề.

    Raises:
        ValueError: Nếu một đỉnh trong graph.edges() không tồn tại trong danh sách nodes.
    """
    adj_list = {node: [] for node in nodes}

    for u_node, v_node in graph.edges():
        if u_node not in adj_list or v_node not in adj_list:
            raise ValueError(f"Đỉnh '{u_node}' hoặc '{v_node}' không tồn tại trong danh sách nodes.")

        # Chỉ thêm cạnh một chiều từ u_node đến v_node.
        adj_list[u_node].append(v_node)

    return adj_list

#Hàm in danh sách kề
def print_adj_list(adj_list):
    """
    In danh sách kề một cách rõ ràng và dễ đọc.

    Args:
        adj_list (dict): Từ điển biểu diễn danh sách kề.
    """
    if not adj_list:
        print("Danh sách kề rỗng.")
        return

    print("Danh sách kề:")
    for node, neighbors in adj_list.items():
        # Chuyển đổi các đỉnh liền kề thành chuỗi để in
        neighbors_str = ", ".join(map(str, sorted(neighbors)))
        print(f"{node}: [{neighbors_str}]")   

