import networkx as nx
import matplotlib.pyplot as plt


#Hàm lưu ảnh đồ thị
def save_graph_image(graph, image_name, pos = None):
    """
    Vẽ đồ thị NetworkX và lưu nó thành file ảnh vào thư mục 'img'.

    Hàm này tạo một Figure Matplotlib từ đối tượng đồ thị NetworkX, 
    sau đó lưu Figure này vào thư mục 'img' (ngang hàng với main.py). 
    Thư mục 'img' sẽ được tạo nếu nó chưa tồn tại.

    Args:
        graph: Đối tượng đồ thị NetworkX đã được khởi tạo 
        image_name: Tên file ảnh muốn lưu
        pos: (Optional) Một dictionary chứa vị trí tùy chỉnh của các đỉnh.  
             Nếu None, hàm sẽ sử dụng nx.spring_layout() để tự động tính toán.

    Returns:
        None: Hàm không trả về giá trị, nhưng in ra thông báo thành công hoặc lỗi.
        
    Raises:
        IOError: Nếu xảy ra lỗi trong quá trình tạo thư mục hoặc lưu file.
    """
    
    # 1. KHỞI TẠO FIGURE
    # fig là đối tượng Figure mà Matplotlib dùng để lưu ảnh
    fig, ax = plt.subplots() # Giữ kích thước mặc định (6.4, 4.8 inches)
    
    # 2. XỬ LÝ VỊ TRÍ ĐỈNH (Layout)
    if pos is None:
        try:
            pos = nx.spring_layout(graph, seed=42)
        except Exception as e:
            print(f"Lỗi khi tính toán layout: {e}")
            plt.close(fig)
            return

    # 3. VẼ ĐỒ THỊ (Sử dụng thuộc tính cơ bản nhất của nx.draw)
    nx.draw(
        graph, 
        pos, 
        with_labels=True, # Hiển thị nhãn đỉnh
        ax=ax # Đảm bảo vẽ lên đối tượng Axes đã tạo
    )

    # Tắt trục tọa độ
    ax.axis('off')
    
    # 4. QUẢN LÝ ĐƯỜNG DẪN VÀ LƯU ẢNH
    from pathlib import Path

    current_dir = Path.cwd()
    image_dir = current_dir / "img"
    save_path = image_dir / image_name
    
    # Tạo thư mục 'img' nếu chưa có
    try:
        image_dir.mkdir(exist_ok=True)
    except Exception as e:
        print(f"❌ Lỗi (IOError): Không thể tạo thư mục '{image_dir.name}': {e}")
        plt.close(fig)
        return

    # Lưu và đóng figure
    try:
        fig.savefig(save_path, bbox_inches='tight') 
        plt.close(fig)
        
        print("---" * 15)
        print(f"✅ Đồ thị đã được lưu thành công tại: {save_path.relative_to(current_dir)}")
        print("---" * 15)
        
    except Exception as e:
        print(f"❌ Lỗi (IOError): Không thể lưu ảnh '{image_name}': {e}")