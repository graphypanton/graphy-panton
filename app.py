
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import requests
from io import BytesIO

st.set_page_config(layout="wide")
st.title("Граф взаимопомощи студентов")

# Прямая ссылка на скачивание с Mail.ru
url = ("https://cloclo21.datacloudmail.ru/weblink/get/"
       "fzhG/jAtvSM34R")
response = requests.get(url)
G = nx.read_graphml(BytesIO(response.content))

fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=300, font_size=8, ax=ax)
st.pyplot(fig)

st.write(f"Узлов: {G.number_of_nodes()} | Связей: {G.number_of_edges()}")

