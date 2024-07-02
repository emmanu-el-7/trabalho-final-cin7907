from veiculo.carro import Carro
from veiculo.moto import Moto
from veiculo import Veiculo
import streamlit as st

st.header('''Home''')
st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/Cadastro.py", label="Cadastro de Veículos", icon="🏎️")
st.page_link("pages/Pesquisa.py", label="Pesquisa de Veículos", icon="🔍")