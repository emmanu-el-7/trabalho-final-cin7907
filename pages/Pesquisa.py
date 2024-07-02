import streamlit as st
from veiculo.carro import Carro
from veiculo.caminhao import Caminhao
from veiculo.moto import Moto

st.header('''Pesquisa de veículos''')

carro = st.checkbox('Carro')
moto = st.checkbox('Moto')
caminhao = st.checkbox('Caminhao')

if carro:
    search_query = st.text_input('')

    if st.button('Pesquisar'):
        df = Carro.getCarrosDataFrame()
        
        if search_query:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        
        st.write("Carros Cadastrados")
        st.dataframe(df)
        
if moto:
    search_query = st.text_input('')

    if st.button('Pesquisar'):
        df = Moto.getMotosDataFrame()
        
        if search_query:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        
        st.write("Carros Cadastrados")
        st.dataframe(df)

if caminhao:
    search_query = st.text_input('')

    if st.button('Pesquisar'):
        df = Caminhao.getCaminhoesDataFrame()
        
        if search_query:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        
        st.write("Carros Cadastrados")
        st.dataframe(df)