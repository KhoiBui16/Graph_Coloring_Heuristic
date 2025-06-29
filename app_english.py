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

# --- Initialize session state ---
def init_session():
    if "graph" not in st.session_state:
        st.session_state.graph = Graph()
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

# --- Reset the entire session ---
def reset_all():
    st.session_state.clear()

# --- Handle user input ---
def handle_input():
    user_input = st.session_state.input_text
    try:
        lines = user_input.strip().splitlines()
        v, e = map(int, lines[0].split())
        names = lines[1].split()
        edge_list = [tuple(line.strip().split()) for line in lines[2:] if line.strip()]
        g = st.session_state.graph
        g.load_graph(v, e, names, edge_list)
        st.success("Graph loaded successfully!")
    except Exception as ex:
        st.error(f"Error while parsing input: {ex}")

# --- Color the next vertex ---
def step_coloring():
    g = st.session_state.graph
    changed = g.step_one_vertex()
    if not changed:
        st.info("Graph is fully colored!")

# --- Color all vertices ---
def full_coloring():
    g = st.session_state.graph
    while g.step_one_vertex():
        pass
    st.success("Graph has been fully colored!")

# --- Main UI ---
def main():
    st.set_page_config(page_title="Graph Coloring", layout="centered")
    st.title("🎨 Graph Coloring using Greedy Heuristic")

    st.markdown("""
    ### 📘 Problem Statement
    Given an undirected simple graph, color the vertices using a **GREEDY ALGORITHM** so that no adjacent vertices have the same color and the total number of colors used is minimized.  
    Colors are represented using 24-bit RGB values, ranging from `0` (black `#000000`) to `16777215` (white `#FFFFFF`).

    #### 🔽 INPUT:
    - First line: two integers `v` and `e`, the number of vertices and edges.
    - Second line: `v` vertex names.
    - Next `e` lines: each contains two vertex names indicating an edge.

    #### 🔼 OUTPUT:
    - A single line of `v` integers — colors assigned to each vertex in the same order as the input.

    #### 📌 Example:
    ```
    Input:
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

    Output:
    0 1 0 2 1 3 4
    ```
    """)

    init_session()
    g = st.session_state.graph

    st.subheader("📥 Input Graph Data")

    st.markdown("""
    📂 [**View sample test cases** here](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/tree/main/test_case)
    """, unsafe_allow_html=True)

    st.text_area(
        "Graph Input",
        key="input_text",
        height=150,
        placeholder="Enter the input in the format shown above...",
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
        if st.button("📥 Load Input"):
            handle_input()

    with col2:
        if st.button("▶ Next Step"):
            step_coloring()

    with col3:
        if st.button("🖌 Full Coloring"):
            full_coloring()

    with col4:
        if st.button("🔄 Reset"):
            reset_all()
            st.rerun()

    if g.v > 0:
        fig = g.draw_graph()
        st.pyplot(fig)
        st.subheader("📊 Graph Status")

        st.write("**🧠 Vertex Info Matrix:**")
        degree_list = [len(g.adjList[i]) for i in range(g.v)]
        df = pd.DataFrame([
            g.nodeNames,
            degree_list,
            g.colors
        ], index=["Vertex", "Initial Degree", "Color"])

        st.dataframe(df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
            'selector': 'th',
            'props': [('background-color', '#f0f0f0'), ('color', 'black')]
        }, {
            'selector': 'td',
            'props': [('background-color', '#fafafa')]
        }]), use_container_width=True)

        used_colors = set(c for c in g.colors if c != -1)
        st.write(f"**🌈 Total colors used:** {len(used_colors)}")

        if st.download_button("📷 Download Graph Image (PNG)", data=fig_to_bytes(fig), file_name="colored_graph.png", mime="image/png"):
            st.success("Image downloaded successfully!")

# Run the app
if __name__ == "__main__":
    main()
