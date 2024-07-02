import streamlit as st
from veiculo.caminhao import Caminhao

st.header('''Cadastro de caminhões''')

marca = st.text_input('Marca')
modelo = st.text_input('Modelo')
cor = st.text_input('Cor')
ano = st.number_input('Ano', min_value=1900, max_value=2100, step=1)
placa = st.text_input('Placa')

if st.button('Cadastrar'):
    caminhao = Caminhao.cadastroCaminhao(cor, marca, modelo, ano, placa)
    st.success(f'Caminhão {modelo} cadastrado com sucesso!')