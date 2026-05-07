import streamlit as st
import networkx as nx
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Граф взаимопомощи")
st.title("Граф взаимопомощи студентов")

@st.cache_data
def load_graph():
    G = nx.read_graphml("graph_dataset.graphml")
    return G

with st.spinner('Загружаю 7.77MB... Ждём 10-15 сек'):
    G = load_graph()

st.success(f"Загружено! Узлов: {G.number_of_nodes()} | Связей: {G.number_of_edges()}")

# Берем топ-400 узлов чтобы не лагало
top_nodes = sorted(G.degree, key=lambda x: x[1], reverse=True)[:400]
H = G.subgraph([n for n, d in top_nodes])

pos = nx.spring_layout(H, seed=42, k=0.8, iterations=15)

edge_x, edge_y = [], []
for edge in H.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

node_x, node_y, node_text, node_size = [], [], [], []
for node in H.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(f"Студент: {node}<br>Связей: {H.degree[node]}")
    node_size.append(H.degree[node] * 2 + 5)

fig = go.Figure()
fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', 
                         line=dict(width=0.3, color='#888'), hoverinfo='none'))
fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers', text=node_text,
                         marker=dict(size=node_size, color=node_size, 
                         colorscale='Viridis', showscale=True, line_width=1)))

fig.update_layout(showlegend=False, hovermode='closest',
                  margin=dict(b=0,l=0,r=0,t=0),
                  xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                  yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

st.plotly_chart(fig, use_container_width=True, height=600)
st.balloons()
st.info("Наведи на точку чтобы увидеть студента. Зумь двумя пальцами.")

