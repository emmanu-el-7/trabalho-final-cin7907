import streamlit as st
from veiculo.carro import Carro
from veiculo.caminhao import Caminhao
from veiculo.moto import Moto

st.header('''Cadastro de veículos''')

carro = st.checkbox('Carro')
moto = st.checkbox('Moto')
caminhao = st.checkbox('Caminhao')

if carro:
    marca = st.text_input('Marca')
    modelo = st.text_input('Modelo')
    cor = st.text_input('Cor')
    ano = st.number_input('Ano', min_value=1900, max_value=2100, step=1)
    placa = st.text_input('Placa')
    if st.button('Cadastrar'):
        carro = Carro.cadastroCarro(cor, marca, modelo, ano, placa)
        carro.setCarros(carro.placa, carro)
        print(carro.getCarros())
        st.success(f'Carro cadastrado com sucesso!')
    
if moto:
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
        
if caminhao:
    marca = st.text_input('Marca')
    modelo = st.text_input('Modelo')
    cor = st.text_input('Cor')
    ano = st.number_input('Ano', min_value=1900, max_value=2100, step=1)
    placa = st.text_input('Placa')
    if st.button('Cadastrar'):
        caminhao = Caminhao.cadastroCaminhao(cor, marca, modelo, ano, placa)
        caminhao.setCaminhoes(caminhao.placa, caminhao)
        print(caminhao.getCaminhoes())
        st.success(f'Caminhão cadastrado com sucesso!')