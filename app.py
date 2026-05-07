
import streamlit as st
import pandas as pd
import networkx as nx
import plotly.express as px

st.set_page_config(page_title="GraphyPANTON", layout="wide")
st.title("GraphyPANTON - GraphML Edition")

uploaded_file = st.file_uploader("Загрузи .graphml / .gexf / .txt", type=["graphml", "gexf", "txt"])

if uploaded_file:
    try:
        G = nx.read_graphml(uploaded_file)
        st.success(f"Граф загружен! Узлов: {G.number_of_nodes()}, Рёбер: {G.number_of_edges()}")
        
        # Достаём все атрибуты узлов в таблицу
        df = pd.DataFrame.from_dict(dict(G.nodes(data=True)), orient='index')
        st.dataframe(df.head())
        
        st.download_button("Скачать nodes.csv", df.to_csv(index=False), "nodes.csv")
        
        if len(df.columns) >= 2:
            x_axis = st.selectbox("Выбери X", df.columns)
            y_axis = st.selectbox("Выбери Y", df.columns)
            fig = px.scatter(df, x=x_axis, y=y_axis, hover_name=df.index)
            st.plotly_chart(fig, use_container_width=True)
            
    except Exception as e:
        st.error(f"Не смог прочитать файл: {e}")
else:
    st.info("Загрузи graphml файл чтобы увидеть узлы и график")