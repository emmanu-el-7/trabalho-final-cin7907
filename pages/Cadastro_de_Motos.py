import streamlit as st
from veiculo.moto import Moto

st.header('''Cadastro de Motos''')

marca = st.text_input('Marca')
modelo = st.text_input('Modelo')
cor = st.text_input('Cor')
ano = st.number_input('Ano', min_value=1900, max_value=2100, step=1)
placa = st.text_input('Placa')

if st.button('Cadastrar'):
    moto = Moto.cadastroMoto(cor, marca, modelo, ano, placa)
    placa = moto.getPlaca()
    print('Testeeeeeee', moto)
    moto.setMotos(placa, moto)
    print('', moto.getMotos())
    st.success(f'Moto cadastrada com sucesso!')