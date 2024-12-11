# README.md

## Hướng dẫn chạy ứng dụng

Để chạy ứng dụng, vui lòng mở và chạy file **app.py**. Đối với thư mục *test*, bạn không cần quan tâm đến nội dung trong đó. Hiện tại, chúng ta chỉ tập trung vào các thư mục và tệp sau đây:

- **Thư mục:** `backend`, `fontend`
- **Tệp:** `app.py`, `rcm_app.py`

---

## Giải thích các thư mục

### 1. Thư mục `backend`
- Chức năng: Thư mục này dùng để truy xuất các dữ liệu dựa trên yêu cầu của người dùng từ máy chủ.

### 2. Thư mục `fontend`
- Chức năng: Chứa các đối tượng tác động đến giao diện hiển thị cho người dùng.

#### Bên trong thư mục `fontend`:

- **Thư mục `animations`:**
  - Chứa các cách thức hoạt động của các hoạt ảnh.
  - Các hoạt ảnh mới sẽ được tạo và lưu tại đây.

- **Thư mục `css`:**
  - Lưu trữ các định dạng cụ thể cho từng đối tượng trong trang web.
  - Tùy chỉnh giao diện theo sở thích, thay thế định dạng mặc định của framework *Streamlit*.
  - Các đối tượng vẫn giữ nguyên chức năng vốn có.

- **Thư mục `screens`:**
  - Chứa các trang được thiết kế để hiển thị cho người dùng.
    - `home_page.py`: Định nghĩa các hàm hiển thị và quản lý giao diện trang chính.
    - `search_by_mood_genres.py`: Hiển thị trang tìm kiếm theo tâm trạng và thể loại, kèm theo kết quả tìm kiếm.
    - `search_by_name.py`: Hiển thị trang tìm kiếm theo tên và kết quả tương ứng.

---

## Các tệp đơn lẻ

### 1. `app.py`
- Chức năng: Tệp này dùng để khởi động ứng dụng.
- Lưu ý: Nhờ [Thuận](https://github.com/mjngxwnj), ứng dụng đã được thiết lập tự động chạy bằng Docker, do đó bạn có thể tạm thời không cần sử dụng chức năng này.

### 2. `rcm_app.py`
- Chức năng: Khởi tạo các trạng thái ban đầu của ứng dụng.
- Quản lý sự chuyển đổi giữa các đối tượng trong ứng dụng.

### 3. `requirements.txt`
- Chức năng: Danh sách các thư viện cần thiết để chạy ứng dụng.



