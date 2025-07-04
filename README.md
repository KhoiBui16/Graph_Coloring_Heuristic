
# Tô Màu Đồ Thị Bằng Chiến Lược Heuristic  

**Họ tên:** Bùi Nhật Anh Khôi  
**MSSV:** 23520761  
**Lớp:** CS112.P22  

[Link github](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/)

[Link demo app](https://graph-coloring.streamlit.app/)

[Link test case](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/tree/main/test_case)

---

## 📚 Mục lục

- [🎯 Mục tiêu bài toán](#-mục-tiêu-bài-toán)
- [💡 Ý tưởng và giải pháp](#-ý-tưởng-và-giải-pháp)
- [📌 Input mẫu](#input-mẫu)
- [✅ Output tương ứng](#output-tương-ứng)
- [📂 Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [⚙️ Các chức năng của ứng dụng](#️-các-chức-năng-của-ứng-dụng)
- [🖼 Minh hoạ giao diện](#-minh-hoạ-giao-diện)
- [🧩 Hướng dẫn sử dụng ứng dụng](#-hướng-dẫn-sử-dụng-ứng-dụng)
- [📺 Video demo quá trình thử nghiệm](#-video-demo-quá-trình-thử-nghiệm)
- [🧪 Hướng dẫn chạy local](#-hướng-dẫn-chạy-local)

---

## 🎯 Mục tiêu bài toán

Bài toán đặt ra là **tô màu các đỉnh của một đồ thị đơn vô hướng**, sao cho thỏa mãn các ràng buộc và tối ưu hóa tiêu chí về số lượng màu sử dụng. Cụ thể, mục tiêu bao gồm:

1. **Không tô trùng màu giữa các đỉnh kề nhau**
2. **Sử dụng ít màu nhất có thể (Greedy heuristic)**
3. **Biểu diễn màu bằng chỉ số RGB 24-bit (0–16777215)**

---

## 💡 Ý tưởng và giải pháp

Ứng dụng hiện thực thuật toán **tô màu đồ thị theo chiến lược tham lam (Greedy Coloring)**. Với mỗi đỉnh chưa được tô màu, thuật toán sẽ:

- Duyệt từng đỉnh theo thứ tự định sẵn
- Tìm màu nhỏ nhất chưa được dùng bởi các đỉnh kề
- Gán màu hợp lệ cho đỉnh đó
- Lặp lại cho đến khi tất cả đỉnh đều được tô màu

Ứng dụng hỗ trợ hai chế độ: **tô toàn bộ tự động** hoặc **tô từng bước**, phù hợp cho mục đích minh hoạ và giảng dạy.

---

## 📌 Input mẫu

```
7 18
J R Q F L P I
L I
L F
F R
F J
L J
J R
J P
F Q
P L
F I
R P
I Q
Q L
F P
J I
I R
P Q
P I
```

---

## ✅ Output tương ứng

```
0 1 0 2 1 3 4
```

---


## 📂 Cấu trúc thư mục

```
├── app.py                      # Giao diện chính sử dụng Streamlit
├── graph_model.py              # Định nghĩa lớp Graph và các thuật toán tô màu
├── requirements.txt            # Danh sách thư viện cần cài đặt
├── README.md                   # File mô tả bài toán, hướng dẫn và giải pháp
├── demo_graph_coloring.mp4     # (Tuỳ chọn) Video demo quá trình chạy ứng dụng
├── test_case/                  # Thư mục chứa các bộ test input/output mẫu
    ├──case1/
        ├──input1.txt
        ├──output1.txt
    ├──case2/
        ├──input2.txt
        ├──output2.txt
    ...
    ├──case5/
      ├──input5.txt
      ├──output5.txt
├── assets/
│   ├── ui_input.png            # Ảnh minh hoạ giao diện nhập input và thao tác
│   └── ui_result.png           # Ảnh minh hoạ giao diện kết quả tô màu

```

---

## ⚙️ Các chức năng của ứng dụng

| Chức năng       | Mô tả |
|-----------------|-------|
| 📥 Đọc dữ liệu   | Nhập đồ thị từ input |
| ▶ Bước tô tiếp  | Tô màu cho 1 đỉnh tiếp theo |
| 🖌 Tô toàn bộ    | Tự động tô toàn bộ |
| 🔄 Thiết lập lại| Xoá trạng thái hiện tại |
| 📷 Tải ảnh đồ thị| Xuất ảnh PNG đồ thị đã tô |

Ngoài ra:
- Hiển thị **bảng trạng thái**: tên đỉnh, bậc, màu.
- Thống kê tổng số màu đã dùng.

---


## 🖼 Minh hoạ giao diện

### 🧩 Giao diện nhập input và thao tác tô màu
![UI Demo](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/blob/main/assets/ui_input.png)

---

### 🎨 Giao diện kết quả sau khi tô màu
![UI Result](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/blob/main/assets/ui_result.png)

---

## 🧩 **Hướng dẫn sử dụng ứng dụng**

1️⃣ Nhập dữ liệu đồ thị
- Tại ô “Toàn bộ input”, hãy nhập dữ liệu đầu vào đúng định dạng như ví dụ:
```
v e
tên_đỉnh_1 tên_đỉnh_2 ... tên_đỉnh_v
đỉnh_u1 đỉnh_v1
đỉnh_u2 đỉnh_v2
...
đỉnh_ue đỉnh_ve
```
Bấm nút 📥 Đọc dữ liệu để khởi tạo đồ thị trong hệ thống.

2️⃣ Tô màu đồ thị
- Sau khi nạp dữ liệu thành công, bạn có thể chọn 1 trong 2 chế độ tô màu:


| Chức năng       | Mô tả |
|-----------------|-------|
| ▶ Bước tô tiếp  | Tô màu cho 1 đỉnh tiếp theo |
| 🖌 Tô toàn bộ    | Tự động tô toàn bộ |

3️⃣ Xem kết quả

Ứng dụng sẽ hiển thị:

- 🎨 Đồ thị đã tô màu (mỗi đỉnh có một màu rõ ràng).

- 📊 Bảng trạng thái gồm: Tên đỉnh, bậc (degree), màu đã gán.

- 🌈 Số màu đã sử dụng tính đến thời điểm hiện tại.

- 📷 Tải ảnh kết quả bằng nút “Tải ảnh đồ thị (PNG)”.

4️⃣ Thiết lập lại

Sử dụng nút 🔄 Thiết lập lại để xoá trạng thái hiện tại và bắt đầu lại từ đầu với input mới.


---

## 📺 Video demo quá trình thử nghiệm

👉 [Link video demo chạy app](https://www.youtube.com/watch?v=fQZRF86sa0k)

---

## 🧪 Hướng dẫn chạy local
Follow these steps to clone and run app on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/KhoiBui16/Graph_Coloring_Heuristic.git
cd Graph_Coloring_Heuristic
```

### 2. Set up your environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then go to: [http://localhost:8501](http://localhost:8501)

---

## 🛠 Tech Stack

- Python 3.x
- Streamlit
- Matplotlib
- NetworkX
- Pandas

---

## 📬 Contact

- 📧 Email: khoibui1601.email@example.com  
- 🐛 Issue: [GitHub Issue Tracker](https://github.com/KhoiBui16/graph-coloring-app/issues)

---
