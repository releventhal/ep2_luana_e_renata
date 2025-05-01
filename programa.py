import funcoes 
cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full house': -1,
        'sequencia baixa': -1,
        'sequencia alta': -1,
        'cinco_iguais': -1   }         }               #cria uma cartela vazia
funcoes.imprime_cartela(cartela)

rodada = 0
while rodada < 12:
    rodada_continua = True
    while rodada_continua:
        print(f'Dados rolados: {funcoes.rolar_dados(5)}')
        print(f'Dados guardados: []')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input(('> '))
        if opcao == 1: 
