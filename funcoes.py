import math 
import random 

def rolar_dados(n):
    lista = []
    for i in range(n):
        dado = random.randint(1, 6) 
        lista.append(dado)
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    if 0 <= dado_para_guardar < len(dados_rolados):
        
        dados_no_estoque.append(dados_rolados[dado_para_guardar])
        
        del dados_rolados[dado_para_guardar]
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    if 0 <= dado_para_remover < len(dados_no_estoque):
        
        dados_rolados.append(dados_no_estoque[dado_para_remover])
        
        del dados_no_estoque[dado_para_remover]
    return [dados_rolados, dados_no_estoque]