import streamlit as st

# --- Display image ---
st.image("LabReport_BSD2513_#1.jpg", caption="Graph Representation", use_container_width=True)

# --- Graph definition ---
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'G', 'E'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G','F']
}

# --- BFS ---
def bfs(graph, start):
    visited, queue = [start], [start]
    order = []

    while queue:
        node = queue.pop(0)
        order.append(node)
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return order

# --- DFS ---
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited, order = [], []
    visited.append(start)
    order.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited, order)
    return order

# --- Streamlit interface ---
start_node = st.selectbox("Select Starting Node:", list(graph.keys()))
algorithm = st.radio("Select Algorithm:", ["BFS", "DFS"])

if st.button("Run"):
    if algorithm == "BFS":
        st.success(" → ".join(bfs(graph, start_node)))
    else:
        st.info(" → ".join(dfs(graph, start_node)))
