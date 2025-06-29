
# 🎨 Graph Coloring Using Greedy Heuristic

**Full Name:** Bui Nhat Anh Khoi 
**Student ID:** 23520761  
**Class:** CS112.P22  

[🔗 GitHub Repository](https://github.com/KhoiBui16/Graph_Coloring_Heuristic)  
[🚀 Live Demo App](https://graph-coloring.streamlit.app/)  
[🧪 Sample Test Cases](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/tree/main/test_case)

---

## 📚 Table of Contents

- [🎯 Problem Objectives](#-problem-objectives)
- [💡 Idea and Solution](#-idea-and-solution)
- [📌 Sample Input](#sample-input)
- [✅ Corresponding Output](#corresponding-output)
- [📂 Project Structure](#-project-structure)
- [⚙️ App Features](#️-app-features)
- [🖼 UI Illustration](#-ui-illustration)
- [🧩 How to Use the App](#-how-to-use-the-app)
- [📺 Demo Video](#-demo-video)
- [🧪 Run Locally](#-run-locally)
- [🛠 Tech Stack](#-tech-stack)
- [📬 Contact](#-contact)

---

## 🎯 Problem Objectives

The problem is to **color the vertices of an undirected simple graph** such that:

1. **No two adjacent vertices share the same color**
2. **The number of colors used is minimized** (using a Greedy heuristic)
3. **Colors are represented in 24-bit RGB format** (range from `0` to `16777215`)

---

## 💡 Idea and Solution

This app implements the **Greedy Coloring algorithm**. For each uncolored vertex, the algorithm:

- Iterates through vertices in a given order
- Finds the **smallest available color** not used by adjacent vertices
- Assigns that color to the vertex
- Repeats until all vertices are colored

The app supports two modes:
- **Step-by-step coloring**
- **Color all at once**

This makes the app suitable for both experimentation and educational purposes.

---

## 📌 Sample Input

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

## ✅ Corresponding Output

```
0 1 0 2 1 3 4
```

---

## 📂 Project Structure

```
├── app.py                    # Main Streamlit UI
├── graph_model.py            # Graph class & coloring logic
├── requirements.txt          # Dependencies
├── README.md                 # This file
├── demo_graph_coloring.mp4   # Optional demo video
├── test_case/                # Input/output test cases
│   ├── case1/
│   │   ├── input1.txt
│   │   └── output1.txt
│   ├── case2/
│   │   ├── input2.txt
│   │   └── output2.txt
│   ...
├── assets/
│   ├── ui_input.png          # Screenshot: input & control
│   └── ui_result.png         # Screenshot: result after coloring
```

---

## ⚙️ App Features

| Feature             | Description                                      |
|---------------------|--------------------------------------------------|
| 📥 Load Input        | Parse graph data from user input                 |
| ▶ Step Coloring      | Color one vertex at a time                       |
| 🖌 Full Coloring      | Automatically color the entire graph            |
| 🔄 Reset             | Reset the graph state                            |
| 📷 Export Image      | Download the colored graph as PNG               |

Additional features:
- Table of vertex state: name, degree, color
- Count of total colors used

---

## 🖼 UI Illustration

### 🧩 Input and Controls Interface  
![UI Input](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/blob/main/assets/ui_input_english.png)

---

### 🎨 Result After Coloring  
![UI Result](https://github.com/KhoiBui16/Graph_Coloring_Heuristic/blob/main/assets/ui_result_english.png)

---

## 🧩 How to Use the App

### 1️⃣ Input Graph Data

- Paste the graph input into the **“Full input”** box in the following format:

```
v e
vertex_1 vertex_2 ... vertex_v
u1 v1
u2 v2
...
ue ve
```

📌 **Example:**
```
7 18
J R Q F L P I
L I
L F
F R
...
P I
```

- Click **📥 Load Input** to initialize the graph.

---

### 2️⃣ Choose Coloring Mode

| Button             | Description                         |
|--------------------|-------------------------------------|
| ▶ Step Coloring     | Color one vertex at a time          |
| 🖌 Full Coloring     | Color the entire graph automatically|

---

### 3️⃣ View the Results

- 🎨 Colored graph visualization  
- 📊 Table of vertex info: name, degree, color  
- 🌈 Total number of colors used  
- 📷 Option to **download the graph image (PNG)**

---

### 4️⃣ Reset the App

Click **🔄 Reset** to clear the current state and input a new graph.

---

## 📺 Demo Video

👉 [Watch the demo on YouTube](https://www.youtube.com/watch?v=fQZRF86sa0k)

---

## 🧪 Run Locally

Follow the steps below to run the app on your machine.

### 1. Clone the repository

```bash
git clone https://github.com/KhoiBui16/graph-coloring-app.git
cd graph-coloring-app
```

### 2. Set up a virtual environment

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

Then open your browser at: [http://localhost:8501](http://localhost:8501)

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
- 🐛 Report issues: [GitHub Issues](https://github.com/KhoiBui16/graph-coloring-app/issues)
