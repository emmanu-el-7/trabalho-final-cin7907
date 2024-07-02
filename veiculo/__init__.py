class Veiculo:
    # carros = {}
    # motos = {}
    # caminhoes = {}
    
    def __init__(self, cor, marca, modelo, ano, placa):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        # self.carros = carros
        # self.motos = motos
        # self.caminhoes = caminhoes
        
    def setCor(self, cor):
        self.cor = cor
        
    def setMarca(self, marca):
        self.marca = marca
        
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def setAno(self, ano):
        self.ano = ano
    
    def setPlaca(self, placa):
        self.placa = placa
        
    # def setCarros(self, placa, carro):
    #     self.__carros[placa] = carro
        
    # def setMotos(self, placa, moto):
    #     self.__motos[placa] = moto
        
    # def setCaminhoes(self, placa, caminhao):
    #     self.__caminhoes[placa] = caminhao
        
    def getCor(self):
        return self.cor
    
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
    
    def getAno(self):
        return self.ano
    
    def getPlaca(self):
        return self.placa
    
    # def getCaminhoes(self):
    #     return self.caminhao
    
    # def getCarros(self):
    #     return self.carro
    
    # def getMotos(self):
    #     return self.moto
    
    @staticmethod
    def cadastroVeiculo(tipo, marca, modelo, cor, ano, placa):
        return tipo(cor, marca, modelo, ano, placa)