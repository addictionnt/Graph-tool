import networkx as nx
import matplotlib.pyplot as plt

#Hàm tìm đường đi ngắn nhất
def find_shortest_path(adj_list, start_node, goal_node):
    """
    Tìm đường đi ngắn nhất (ít cạnh nhất) từ nút bắt đầu đến nút kết thúc
    sử dụng thuật toán Duyệt theo Chiều Rộng (Breadth-First Search - BFS).
    Args:
        adj_list (dict): Danh sách kề của đồ thị
        start_node: Tên của nút bắt đầu.
        goal_node: Tên của nút đích.

    Returns:
        tuple: Tuple (Đường đi ngắn nhất).
               Trả về [] nếu không tìm thấy đường đi hoặc nút không hợp lệ.
    """
    # 1. Kiểm tra và Khởi tạo
    if start_node not in adj_list or goal_node not in adj_list:
        if start_node == goal_node:
            return [start_node], 0
        return [], 0
    from collections import deque
    
    queue = deque([start_node])
    visited = {start_node}
    # came_from: Lưu trữ nút tiền nhiệm (predecessor)
    came_from = {node: None for node in adj_list}

    # 2. Vòng lặp BFS
    while queue:
        current_node = queue.popleft()

        if current_node == goal_node:
            break

        for neighbor in adj_list.get(current_node, []):
            if neighbor not in visited:
                came_from[neighbor] = current_node
                visited.add(neighbor)
                queue.append(neighbor)
    
    # 3. Tái tạo đường đi
    # Nếu nút đích không có nút tiền nhiệm, nghĩa là không thể đến được (trừ khi start=goal)
    if came_from.get(goal_node) is None and start_node != goal_node:
        return [], 0
    
    path = []
    current = goal_node
    
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    
    path.reverse()
    
    return path if path and path[0] == start_node else []

#Hàm chuyển path thành edges
def path_to_edges(path):
    """
    Chuyển đổi danh sách các đỉnh của một đường đi thành danh sách các cạnh có hướng.

    Hàm tạo ra các cặp (u, v) liên tiếp từ danh sách các nút,
    biểu diễn thứ tự các cạnh trong đường đi.

    Args:
        path (list): Danh sách các nút theo thứ tự của đường đi.

    Returns:
        list of tuple: Danh sách các cặp tuple (nút nguồn, nút đích) biểu diễn 
                       các cạnh của đường đi.
    """
    edges = []
    
    # Lặp qua danh sách từ nút đầu tiên đến nút kế cuối.
    # Mỗi lần lặp tạo ra một cạnh nối nút hiện tại với nút kế tiếp.
    for i in range(len(path) - 1):
        source_node = path[i]
        target_node = path[i + 1]
        
        edges.append((source_node, target_node))
        
    return edges
