import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GraphyPANTON", layout="wide")
st.title("GraphyPANTON")
st.write("Interactive graph visualization platform with PANTONE-styled export")

uploaded_file = st.file_uploader("Загрузи results.csv", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
    
    x_axis = st.selectbox("Выбери X", df.columns)
    y_axis = st.selectbox("Выбери Y", df.columns)
    
    fig = px.scatter(df, x=x_axis, y=y_axis)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Загрузи CSV файл чтобы построить график")
