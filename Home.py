from veiculo.carro import Carro
from veiculo.moto import Moto
from veiculo import Veiculo
import streamlit as st

st.header('''Home''')
st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/Cadastro_de_Carros.py", label="Cadastro de Carros", icon="🏎️")
st.page_link("pages/Cadastro_de_Motos.py", label="Cadastro de Motos", icon="🏍️")
st.page_link("pages/Cadastro_de_Caminhões.py", label="Cadastro de Caminhões", icon="🚚")
st.page_link("pages/Página_de_Carros.py", label="Pesquisa de Carros", icon="🏎️")
st.page_link("pages/Página_de_Motos.py", label="Pesquisa de motos", icon="🏍️")
st.page_link("pages/Página_de_Caminhões.py", label="Pesquisa de Caminhões", icon="🚚")



