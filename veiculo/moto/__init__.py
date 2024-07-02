from veiculo import Veiculo
import pandas as pd

class Moto(Veiculo):
    '''Subclasse para motos'''
    __motos = {}
    def __init__(self, cor, marca, modelo, ano, placa):
        super().__init__(cor, marca, modelo, ano, placa)
        self.__cor = cor
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__placa = placa
        
    def setCor(self, cor):
        self.__cor = cor
        
    def setMarca(self, marca):
        self.__marca = marca
        
    def setModelo(self, modelo):
        self.__modelo = modelo
    
    def setAno(self, ano):
        self.__ano = ano
    
    def setPlaca(self, placa):
        self.__placa = placa
        
        
    @classmethod
    def setMotos(cls, placa, moto):
        cls.__motos[placa] = moto
        
    def getCor(self):
        return self.__cor
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAno(self):
        return self.__ano
    
    def getPlaca(self):
        return self.__placa
    
    @classmethod
    def getMotos(cls):
        return cls.__motos
    
    @staticmethod
    def cadastroMoto(cor, marca, modelo, ano, placa):
        return Veiculo.cadastroVeiculo(Moto, marca, modelo, cor, ano, placa)
    
    @classmethod
    def getMotosDataFrame(cls):
        motos = cls.getMotos()
        data = {
            'Marca': [moto.marca for moto in motos.values()],
            'Modelo': [moto.modelo for moto in motos.values()],
            'Cor': [moto.cor for moto in motos.values()],
            'Ano': [moto.ano for moto in motos.values()],
            'Placa': [moto.placa for moto in motos.values()]
        }
        return pd.DataFrame(data)