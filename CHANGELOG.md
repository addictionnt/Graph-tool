# [0.1.8] - 2025-09-27

### ✨ Added (Tính năng mới)

- 🖼️ **Ra mắt hàm `save_graph_image_with_highlights()`:** Đã bổ sung hàm mới cho phép vẽ và lưu ảnh đồ thị, trong đó các **cạnh được chỉ định có thể được tô màu** (mặc định là màu đỏ).
    - Tính năng này rất hữu ích cho việc trực quan hóa **kết quả thuật toán** như đường đi ngắn nhất (shortest paths) hoặc luồng tối đa (maximum flow).
    - Hàm sử dụng `pathlib` để quản lý I/O và tự động tạo thư mục `img/`.

# [0.1.7] - 2025-09-27

### 🐛 Fixed (Sửa lỗi)

-   **Tính nhất quán của `find_shortest_path()`:** Đã sửa lỗi logic trong hàm `find_shortest_path()`. Hàm này hiện đã **nhất quán** trả về một **list rỗng** (`[]`) trong tất cả các trường hợp không tìm thấy đường đi hoặc nút không hợp lệ.
    -   Trước đây, hàm có thể trả về `([], 0)` (một tuple) hoặc `[]` (một list), gây ra sự không nhất quán trong kiểu dữ liệu trả về.
    -   Hàm hiện tại chỉ trả về **list** (list đường đi nếu thành công, `[]` nếu thất bại).

## [0.1.6] - 2025-09-27

### ✨ Added (Thêm mới)

-   **Thêm Module Thuật toán Đồ thị Cơ bản (BFS):**
    -   `find_shortest_path()`: Triển khai thuật toán **Duyệt theo Chiều Rộng (BFS)** để tìm đường đi ngắn nhất (ít cạnh nhất) giữa hai nút trong đồ thị được biểu diễn bằng danh sách kề.
    -   `path_to_edges()`: Chức năng tiện ích để chuyển đổi danh sách các nút của một đường đi thành danh sách các cạnh (tuple).
-   **Thêm Tính năng Trực quan hóa Nổi bật:**
    -   `show_graph_with_egdes_to_highlight()`: Cho phép vẽ đồ thị (sử dụng NetworkX) và **tô màu đỏ** cho một tập hợp các cạnh cụ thể (ví dụ: đường đi ngắn nhất). Hỗ trợ đồ thị có hướng và vô hướng.

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
