import funcoes 
cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1   }         }               #cria uma cartela vazia
funcoes.imprime_cartela(cartela)

rodada = 0
while rodada < 12:
    ja_rerrolou = 0
    dados_rolados = funcoes.rolar_dados(5)
    dados_guardados = []
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')
    rodada_continua = True
    while rodada_continua:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input(('> '))
        if opcao == '1': 
            print("Digite o índice do dado a ser guardado (0 a 4):")
            dado_guardar = input(('> '))
            lista_pos_guardar = funcoes.guardar_dado(dados_rolados, dados_guardados, int(dado_guardar))
            dados_rolados = lista_pos_guardar[0]
            dados_guardados = lista_pos_guardar[1]
            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')
        elif opcao =='2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            dado_remover = input(('> '))
            lista_pos_remover = funcoes.remover_dado(dados_rolados, dados_guardados, int(dado_remover))
            dados_rolados = lista_pos_remover[0]
            dados_guardados = lista_pos_remover[1]
            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')
        elif opcao == '3':
            if ja_rerrolou >= 2:
                print("Você já usou todas as rerrolagens.")
                print(f'Dados rolados: {dados_rolados}')
                print(f'Dados guardados: {dados_guardados}')
            else: 
                qtd = len(dados_rolados)
                dados_rolados = funcoes.rolar_dados(qtd) 
                print(f'Dados rolados: {dados_rolados}')
                print(f'Dados guardados: {dados_guardados}')
                ja_rerrolou += 1
        elif opcao == '4':
            funcoes.imprime_cartela(cartela)
        elif opcao == '0':
            print("Digite a combinação desejada:")
            combinacao = input(('> '))
            cats_av = cartela['regra_avancada']
            cats_simp = cartela['regra_simples']
            if combinacao not in ['1', '2', '3', '4', '5', '6']: 
                while combinacao not in cats_av:
                    print("Combinação inválida. Tente novamente.") 
                    combinacao = input(('> '))
            else:
                while int(combinacao) not in cats_simp:
                    print("Combinação inválida. Tente novamente.") 
                    combinacao = input(('> '))
            if combinacao in cats_av:
                while cats_av[combinacao] != -1:
                    print("Essa combinação já foi utilizada.")
                    combinacao = input(('> '))
            if combinacao in cats_simp:
                while cats_simp[int(combinacao)] != -1:
                    print("Essa combinação já foi utilizada.")
                    combinacao = input(('> '))
            cartela = funcoes.faz_jogada(dados_guardados, combinacao, cartela) 
            funcoes.imprime_cartela(cartela) 
            rodada_continua = False
    rodada += 1  
   
        
print("Fim do jogo!")
funcoes.imprime_cartela(cartela)

total_pontos = sum(p for p in cartela['regra_simples'].values()) + sum(p for p in cartela['regra_avancada'].values())

pontos_simples = sum(p for p in cartela['regra_simples'].values())
if pontos_simples >= 63:
    total_pontos += 35

print(f"Pontuação total: {total_pontos}")
   