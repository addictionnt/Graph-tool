## [0.1.5] - 2025-09-26

### ✨ Added (Thêm mới)

-   **Thêm tính năng Lưu Trực quan hóa Đồ thị:**
    -   `save_graph_image()`: Cho phép người dùng **vẽ và lưu đồ thị** (sử dụng NetworkX và Matplotlib) thành file ảnh.
    -   Ảnh đồ thị được lưu mặc định vào thư mục **`img/`** (sẽ được tạo tự động nếu chưa tồn tại).
    -   Hỗ trợ tùy chọn vị trí đỉnh (`pos`) tùy chỉnh, hoặc tự động tính toán layout.

## [0.1.4] - 2025-09-25

### ✨ Added (Thêm mới)

-   **Thêm các hàm tạo và hiển thị ma trận/danh sách kề (Adjacency Matrix/List):**
    -   `create_adj_matrix_undirected()`: Tạo ma trận kề cho đồ thị vô hướng.
    -   `create_adj_matrix_directed()`: Tạo ma trận kề cho đồ thị có hướng.
    -   `print_adj_matrix()`: In ma trận kề một cách dễ đọc.
    -   `create_adj_list_undirected()`: Tạo danh sách kề cho đồ thị vô hướng.
    -   `create_adj_list_directed()`: Tạo danh sách kề cho đồ thị có hướng.
    -   `print_adj_list()`: In danh sách kề một cách dễ đọc.

## [0.1.3] - 2025-09-25

### ✨ Added (Thêm mới)

-   **Thêm các hàm kiểm tra tính liên thông của đồ thị (Connectivity Checks):**
    -   `check_undirected_connectivity()`: Kiểm tra xem đồ thị vô hướng có liên thông hay không.
    -   `check_directed_connectivity()`: Kiểm tra xem đồ thị có hướng có liên thông mạnh hay không.

## [0.1.2] - 2025-09-25

### ✨ Added (Thêm mới)

-   **Thêm các hàm hỗ trợ về đỉnh:**
    -   `get_node_degree`: Lấy bậc của đỉnh.
    -   `get_node_neighbors`: Lấy các đỉnh liền kề.
    -   `get_node_info`: Lấy thông tin đỉnh.

## [0.1.1] - 2025-09-25

### ✨ Added (Thêm mới)

-   **Ra mắt chính thức thư viện `graph_thanhchinh`!**
-   **Cung cấp các chức năng cốt lõi** để tạo, chỉnh sửa và trực quan hóa dữ liệu đồ thị (graphs) ban đầu.
-   **Thêm các hàm tạo và hiển thị đồ thị:**
    -   `create_graph_by_nodes_and_edge()`: Tạo đồ thị vô hướng.
    -   `create_digraph_by_nodes_and_edge()`: Tạo đồ thị có hướng (digraph).
    -   `show_graph()`: Hiển thị đồ thị đã tạo.
