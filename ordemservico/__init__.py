class OrdemServico:
    def __init__(self):
        self._data = ''
        self._problema = ''
        self._orcamento = ''
        self._pago = bool
        self._veiculo = ''
        
    def setData(self, data):
        self._data = data
        
    def setProblema(self, problema):
        self._problema = problema
        
    def setOrcamento(self, orcamento):
        self._orcamento = orcamento
        
    def setPago(self, pago):
        self._pago = pago
        
    def setVeiculo(self, veiculo):
        self._veiculo = veiculo
        
    def getData(self):
        return self._data
    
    def getProblema(self):
        return self._problema
    
    def getOrcamento(self):
        return self._orcamento
    
    def getPago(self):
        return self._pago
    
    def getVeiculo(self):
        return self._veiculo
    
    def imprime(self):
        print('O veículo ', self._veiculo, 'apresentou na data', self._data, 'o seguinte defeito: ', self._problema, '. Valor final ficará em: ', self._orcamento )
