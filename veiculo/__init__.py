class Veiculo:
    def __init__(self, cor, marca, modelo, ano, placa):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        
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
    
    # def cadastroVeiculo(dicionario):
        
    #     tipo = str(input('Qual o tipo de veículo? (Carro, Moto, Caminhão) ')).capitalize()
    #     marca = str(input(f'Qual a marca do(a) {tipo}? '))
    #     modelo = str(input(f'Qual a marca do(a) {marca}? '))
    #     cor = str(input(f'Qual a cor do(a) {modelo}? '))
    #     ano = str(input(f'Qual o ano do(a) {modelo}? '))
    #     placa = str(input(f'Qual a placa do(a) {modelo}? '))
        
    #     dicionario[placa] = tipo(marca, modelo, cor, ano, placa)
        
    #     return print(f'{tipo} cadastrado(a) com sucesso!!')
    
    @staticmethod
    def cadastroVeiculo(tipo, marca, modelo, cor, ano, placa):
        return tipo(cor, marca, modelo, ano, placa)

