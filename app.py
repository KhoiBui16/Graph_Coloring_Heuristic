import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from graph_model import Graph

# --- Helper to convert matplotlib fig to bytes for download ---
def fig_to_bytes(fig):
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    return buf

# --- Hàm khởi tạo trạng thái ban đầu ---
def init_session():
    if "graph" not in st.session_state:
        st.session_state.graph = Graph()
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

# --- Hàm xử lý reset toàn bộ ---
def reset_all():
    st.session_state.clear()

# --- Hàm xử lý đọc input người dùng ---
def handle_input():
    user_input = st.session_state.input_text
    try:
        lines = user_input.strip().splitlines()
        v, e = map(int, lines[0].split())
        names = lines[1].split()
        edge_list = [tuple(line.strip().split()) for line in lines[2:] if line.strip()]
        g = st.session_state.graph
        g.load_graph(v, e, names, edge_list)
        st.success("Đã nạp đồ thị!")
    except Exception as ex:
        st.error(f"Lỗi khi đọc input: {ex}")

# --- Hàm thực hiện bước tô màu tiếp theo ---
def step_coloring():
    g = st.session_state.graph
    changed = g.step_one_vertex()
    if not changed:
        st.info("Đã tô màu xong!")

# --- Hàm tô toàn bộ đến khi xong ---
def full_coloring():
    g = st.session_state.graph
    while g.step_one_vertex():
        pass
    st.success("Đã tô toàn bộ xong!")

# --- Giao diện chính ---
def main():
    st.set_page_config(page_title="Tô màu đồ thị", layout="centered")
    st.title("🎨 Tô màu đồ thị theo chiến lược Heuristic")

    st.markdown("""
    ### 📘 Đề bài
    Cho một đơn đồ thị vô hướng. Hãy tô màu cho đồ thị bằng **PHƯƠNG PHÁP THAM LAM** sao cho các đỉnh lân cận nhau không trùng màu với nhau và số màu phải dùng là nhỏ nhất có thể. 
    Màu được sử dụng là hệ màu RGB 24 bit với tối đa hơn 16 triệu màu, các màu được đánh số từ `0` (màu đen `#000000`) đến `16777215` (màu trắng `#FFFFFF`).

    #### 🔽 INPUT:
    - Dòng đầu tiên chứa 2 số `v`, `e` lần lượt là số đỉnh và số cạnh.
    - Dòng thứ 2 chứa `v` chuỗi (tên các đỉnh).
    - `e` dòng tiếp theo, mỗi dòng chứa 2 tên đỉnh có cạnh nối với nhau.

    #### 🔼 OUTPUT:
    - Một dòng gồm `v` số nguyên — là màu của từng đỉnh, theo đúng thứ tự xuất hiện trong input.

    #### 📌 Ví dụ:
    Input:
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
    
    Output:
    ```
    0 1 0 2 1 3 4
    ```
    """)

    init_session()
    g = st.session_state.graph

    st.subheader("📥 Nhập input theo đề bài")
    
    st.markdown(
    """
    📂 [**Xem các test case mẫu** tại đây:](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/tree/main/test_case)
    """,
    unsafe_allow_html=True
    )
    
    st.text_area(
        "Toàn bộ input",
        key="input_text",
        height=150,
        placeholder="Nhập dữ liệu input theo đúng định dạng đề bài...",
    )

    st.markdown("""
        <style>
        textarea[data-testid="stTextArea"] {
            height: auto !important;
            min-height: 100px;
            overflow-y: auto;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        if st.button("📥 Đọc dữ liệu"):
            handle_input()

    with col2:
        if st.button("▶ Bước tô tiếp"):
            step_coloring()

    with col3:
        if st.button("🖌 Tô toàn bộ"):
            full_coloring()

    with col4:
        if st.button("🔄 Thiết lập lại"):
            reset_all()
            st.rerun()

    if g.v > 0:
        fig = g.draw_graph()
        st.pyplot(fig)
        st.subheader("📊 Trạng thái của đồ thị")

        st.write("**🧠 Ma trận thông tin:**")
        degree_list = [len(g.adjList[i]) for i in range(g.v)]
        df = pd.DataFrame([
            g.nodeNames,
            degree_list,
            g.colors
        ], index=["Tên đỉnh", "Bậc ban đầu", "Màu"])

        st.dataframe(df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
            'selector': 'th',
            'props': [('background-color', '#f0f0f0'), ('color', 'black')]
        }, {
            'selector': 'td',
            'props': [('background-color', '#fafafa')]
        }]), use_container_width=True)

        used_colors = set(c for c in g.colors if c != -1)
        st.write(f"**🌈 Số màu đã sử dụng:** {len(used_colors)}")

        if st.download_button("📷 Tải ảnh đồ thị (PNG)", data=fig_to_bytes(fig), file_name="do_thi.png", mime="image/png"):
            st.success("Tải ảnh thành công!")

# Gọi hàm main
if __name__ == "__main__":
    main()
