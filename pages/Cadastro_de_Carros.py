import streamlit as st
from veiculo.carro import Carro

st.header('''Cadastro de carros''')

marca = st.text_input('Marca')
modelo = st.text_input('Modelo')
cor = st.text_input('Cor')
ano = st.number_input('Ano', min_value=1900, max_value=2100, step=1)
placa = st.text_input('Placa')

if st.button('Cadastrar'):
    carro = Carro.cadastroCarro(cor, marca, modelo, ano, placa)
    st.success(f'Carro {modelo} cadastrado com sucesso!')