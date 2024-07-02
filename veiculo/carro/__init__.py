from veiculo import Veiculo

class Carro(Veiculo):
    '''Subclasse para carros'''
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

    # def cadastroCarro(tipo):
    #     Veiculo.cadastroVeiculo('Carro')
    
    @staticmethod
    def cadastroCarro(cor, marca, modelo, ano, placa):
        return Veiculo.cadastroVeiculo(Carro, marca, modelo, cor, ano, placa)
    
    