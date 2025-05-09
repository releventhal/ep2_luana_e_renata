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

def calcula_pontos_regra_simples(dados):
    pontos = {}
    for i in range(1, 7):
        pontos[i] = 0  

    for dado in dados:
        if 1 <= dado <= 6:
            pontos[dado] += dado

    return pontos

def calcula_pontos_soma(dados):
    soma = 0
    for n in dados:
        soma += n
    return soma

def calcula_pontos_sequencia_baixa(dados):
    novos = []
    for n in dados:
        if n not in novos:
            novos.append(n)

    for i in range(len(novos)):
        for j in range(i + 1, len(novos)):
            if novos[i] > novos[j]:
                novos[i], novos[j] = novos[j], novos[i]

    contagem = 1
    for i in range(1, len(novos)):
        if novos[i] == novos[i - 1] + 1:
            contagem += 1
            if contagem >= 4:
                return 15
        else:
            contagem = 1

    return 0

def calcula_pontos_sequencia_alta(dados):
    novos = []
    for n in dados:
        if n not in novos:
            novos.append(n)

    for i in range(len(novos)):
        for j in range(i + 1, len(novos)):
            if novos[i] > novos[j]:
                novos[i], novos[j] = novos[j], novos[i]

    contagem = 1
    for i in range(1, len(novos)):
        if novos[i] == novos[i - 1] + 1:
            contagem += 1
            if contagem >= 5:
                return 30
        else:
            contagem = 1

    return 0

def calcula_pontos_full_house(dados):
    contagem = {}

    for n in dados:
        if n in contagem:
            contagem[n] += 1
        else:
            contagem[n] = 1

    tres_iguais = False
    dois_iguais = False

    for iguais in contagem.values():
        if iguais == 3:
            tres_iguais = True
        elif iguais == 2:
            dois_iguais = True

    if tres_iguais and dois_iguais:
        soma = 0
        for n in dados:
            soma += n
        return soma
    else:
        return 0

def calcula_pontos_quadra(lista):
    dicio = {}
    for n in lista:
        if n in dicio:
            dicio[n] += 1
        else:
            dicio[n] = 1 
    quatro_iguais = False
    for qtd in dicio.values():
        if qtd >= 4: 
            quatro_iguais = True
    soma = 0
    if quatro_iguais:
        for n in lista:
            soma += n
        return soma 
    else:
        return 0

def calcula_pontos_quina(lista):
    dicio = {}
    for n in lista:
        if n in dicio:
            dicio[n] += 1
        else:
            dicio[n] = 1 
    cinco_iguais = False
    for qtd in dicio.values():
        if qtd >= 5:
            cinco_iguais = True
    if cinco_iguais:
        return 50
    else:
        return 0


def calcula_pontos_regra_avancada(lista):
    dicio = {}
    dicio['cinco_iguais'] = calcula_pontos_quina(lista)
    dicio['full_house'] = calcula_pontos_full_house(lista)
    dicio['quadra'] = calcula_pontos_quadra(lista)
    dicio['sem_combinacao'] = calcula_pontos_soma(lista)
    dicio['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    dicio['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)
    return dicio 

def faz_jogada(lista, categoria, dicio):
    dicio_pontuacao_avancada = calcula_pontos_regra_avancada(lista)
    dicio_pontuacao_simples = calcula_pontos_regra_simples(lista)
    if categoria in dicio_pontuacao_avancada:
        pontuacao = dicio_pontuacao_avancada[categoria] 
        dicio['regra_avancada'][categoria] = pontuacao 
    else:
        pontuacao = dicio_pontuacao_simples[int(categoria)]
        dicio['regra_simples'][int(categoria)] = pontuacao
     
    return dicio

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)