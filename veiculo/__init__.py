class Veiculo:
    def __init__(self):
        self._cor = ''
        self._marca = ''
        self._modelo = ''
        self._ano = ''
        self._placa = ''
        
    def setCor(self, cor):
        self._cor = cor
        
    def setMarca(self, marca):
        self._marca = marca
        
    def setModelo(self, modelo):
        self._modelo = modelo
    
    def setAno(self, ano):
        self._ano = ano
    
    def setPlaca(self, placa):
        self._placa = placa
        
    def getCor(self):
        return self._cor
    
    def getMarca(self):
        return self._marca
    
    def getModelo(self):
        return self._modelo
    
    def getAno(self):
        return self._ano
    
    def getPlaca(self):
        return self._placa