from ordemservico import OrdemServico

ordem1 = OrdemServico()

ordem1.setData('01/07/2024')
ordem1.setProblema('Motor fundido')
ordem1.setOrcamento('R$ 6000')
ordem1.setVeiculo('Palio 2001')

print(ordem1.imprime())