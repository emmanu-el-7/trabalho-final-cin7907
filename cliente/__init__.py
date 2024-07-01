class Cliente:
    def __init__(self):
        self._nome = ''
        self.contato = ''
        self.cpf = ''
        self.veiculos = ''
        
    def setNome(self, nome):
        self._nome = nome
        
    def setContato(self, contato):
        self._contato = contato
        
    def setCpf(self, cpf):
        self._cpf = cpf
        
    def setVeiculos(self, veiculos):
        self._veiculos = veiculos
    
    def getNome(self):
        return self._nome
    
    def getContato(self): 
        return self._contato
    
    def getVeiculos(self):
        return self._veiculos