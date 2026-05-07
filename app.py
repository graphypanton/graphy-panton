
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Граф взаимопомощи студентов")

# Читаем файл прямо из репозитория
G = nx.read_graphml("graph_dataset.graphml")

fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=300, font_size=8, ax=ax)
st.pyplot(fig)

st.write(f"Узлов: {G.number_of_nodes()} | Связей: {G.number_of_edges()}")

