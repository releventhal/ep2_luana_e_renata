import funcoes 
cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1   }         }               #cria uma cartela vazia
funcoes.imprime_cartela(cartela)


cats_regra_simples = ['1', '2', '3', '4', '5', '6']
cats_regra_avan = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']


rodada = 0                  # inicia a contagem de rodadas 
while rodada < 12:
    ja_rerrolou = 0
    dados_rolados = funcoes.rolar_dados(5)          #rolagem inicial 
    dados_guardados = []
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')
    rodada_continua = True
    while rodada_continua:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()
        if opcao == '1':                    #programa para guardar o dado
            print("Digite o índice do dado a ser guardado (0 a 4):")
            dado_guardar = input()
            lista_pos_guardar = funcoes.guardar_dado(dados_rolados, dados_guardados, int(dado_guardar))
            dados_rolados = lista_pos_guardar[0]
            dados_guardados = lista_pos_guardar[1]
            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')
        elif opcao =='2':             #programa para remover o dado 
            print("Digite o índice do dado a ser removido (0 a 4):")
            dado_remover = input()
            lista_pos_remover = funcoes.remover_dado(dados_rolados, dados_guardados, int(dado_remover))
            dados_rolados = lista_pos_remover[0]
            dados_guardados = lista_pos_remover[1]
            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')
        elif opcao == '3':              #programa para rolar de novo (o ja_rerrolou é zerado a cada rodada)
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
        elif opcao == '4':             #imprime a cartela
            funcoes.imprime_cartela(cartela)
        elif opcao == '0': 
            dados_totais = dados_guardados + dados_rolados                   #jogada 
            print("Digite a combinação desejada:")
            cat = input()
            while cat not in cats_regra_avan and cat not in cats_regra_simples:
                print("Combinação inválida. Tente novamente.")
                cat = input()
            if cat in cats_regra_simples:
                while cartela['regra_simples'][int(cat)] != -1:
                    print("Essa combinação já foi utilizada.")
                    cat = input()
            if cat in cats_regra_avan:
                while cartela['regra_avancada'][cat] != -1:
                    print("Essa combinação já foi utilizada.")
                    cat = input()  
    
            cartela = funcoes.faz_jogada(dados_totais, cat, cartela) 
            # funcoes.imprime_cartela(cartela) 
            rodada_continua = False
        else:
            print('Opção inválida. Tente novamente.')
    rodada += 1  
   
        

funcoes.imprime_cartela(cartela)

total_pontos = sum(p for p in cartela['regra_simples'].values()) + sum(p for p in cartela['regra_avancada'].values())

pontos_simples = sum(p for p in cartela['regra_simples'].values())
if pontos_simples >= 63:
    total_pontos += 35

print(f"Pontuação total: {total_pontos}")



