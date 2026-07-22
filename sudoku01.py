# VAMO JOGAR SUDOKUUUUUUU EBAAA

# primeiro fazer o tabuleiro ne bis, vai ter q fazer tipo uma matriz tlg
# vo ter q organizar saporra
import random


# TABULEIRO AQUI
def criar_tabuleiro():
    tabuleiro = []

    for i in range(9):
        linha = []

        for j in range(9):
            linha.append(0)
        tabuleiro.append(linha)
    
    return tabuleiro



# VAI MOSTRAR O TABULEIRO
def mostrar(tabuleiro):
    print("+-------+-------+-------+")
    
    for i in range(9):
        print("| ", end="")

        for j in range(9):
            if tabuleiro[i][j] == 0:
                print(".", end=" ")
            else:
                print(tabuleiro[i][j], end=" ")
                    
            if (j + 1) % 3 == 0:
                print("| ", end="")
                    
        print()
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")



# VERIFICACOES
def pode_colocar(tabuleiro, linha, coluna, numero):
    
    for i in range(9): # esse treco q vai ver se tem numero na linha
        if tabuleiro[linha][i] == numero:
            return False
            
    for i in range(9): # esse verifica na coluna
        if tabuleiro[i][coluna] == numero:
            return False
            
    # dai esse é o 3x3
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if tabuleiro[i][j] == numero:
                return False
                
    return True



# O ROLE DA POSICAO VAZIA
def encontrar_vazio(tabuleiro):
    
    for linha in range(9):
        for coluna in range(9):
            
            if tabuleiro[linha][coluna] == 0:
                return (linha, coluna)
    return None



# BACKTRACKING
# é oq vai fazer "olhar pra tras"
def resolver(tabuleiro):
    
    posicao = encontrar_vazio(tabuleiro)
    
    if posicao is None:
        return True
        
    linha, coluna = posicao
    
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numeros)


    for numero in numeros:
        if pode_colocar(tabuleiro, linha, coluna, numero):
            tabuleiro[linha][coluna] = numero

            if resolver(tabuleiro):
                return True
            
            tabuleiro[linha][coluna] = 0
    return False



# REMOVER OS NUMEROS
# nao sei oq esse faz, mas acho q é remover ne
def remover_numeros(tabuleiro, quantidade):
    while quantidade > 0:

        linha = random.randint(0,8)
        coluna = random.randint(0,8)

        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            quantidade -= 1



# CRIAR NOVA PARTIDA
def novo_jogo(dificuldade):
    tabuleiro = criar_tabuleiro()
    resolver(tabuleiro)

    solucao = []

    for linha in tabuleiro:
        solucao.append(linha.copy())

    if dificuldade == 1:
        remover_numeros(tabuleiro, 30)
    elif dificuldade == 2:
        remover_numeros(tabuleiro, 40)
    elif dificuldade == 3:
        remover_numeros(tabuleiro, 50)

    fixos = []

    for linha in tabuleiro:
        nova_linha = []

        for valor in linha:
            if valor == 0:
                nova_linha.append(False)
            else:
                nova_linha.append(True)
        
        fixos.append(nova_linha)

    return tabuleiro, solucao, fixos




# NAOPSEI
def pedir_numero(mensagem, minimo, maximo):
    while True:
        try:
            numero = int(input(mensagem))

            if minimo <= numero <= maximo:
                return numero
            else:
                print(f"Digite um numero entre {minimo} e {maximo}")

        except ValueError:
            print("Digite apenas numeros")



# VENCEU
def venceu(tabuleiro, solucao):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] != solucao[linha][coluna]:
                return False
    return True



# MENU
def menu():
    while True:
        print("\n====================================")
        print("            S U D O K U")
        print("====================================")
        print("1 - Novo jogo")
        print("2 - Como jogar")
        print("3 - Sair")
        print("====================================")

        opcao = pedir_numero("Escolha uma opção: ", 1, 3)

        if opcao == 1:
            print("\nEscolha a dificuldade")
            print("1 - Facil")
            print("2 - Medio")
            print("3 - Dificil")
            dificuldade = pedir_numero("Opcao: ", 1, 3)

            while True:

                tabuleiro, solucao, fixos = novo_jogo(dificuldade)
                resultado = jogar(tabuleiro, solucao, fixos)

                print("\n==============================")
                print("1 - Jogar novamente")
                print("2 - Voltar ao menu")
                print("3 - Sair")

                escolha = pedir_numero("Opcao: ", 1 ,3)

                if escolha == 1:
                    continue
                elif escolha == 2:
                    break
                elif escolha == 3:
                    return

        elif opcao == 2:
            print("\n========== COMO JOGAR ==========")
            print("Complete o Sudoku preenchendo")
            print("todas as casas vazias.")
            print()
            print("Cada linha deve conter")
            print("os números de 1 a 9.")
            print()
            print("Cada coluna também.")
            print()
            print("Cada bloco 3x3 também.")
            input("\nPressione ENTER para voltar ao menu.")

        elif opcao == 3:
            print("\nByebye")
            break

# JOGAR?
def jogar(tabuleiro, solucao, fixos):

    while True:
        mostrar(tabuleiro)

        print("\nDigite a sua jogada:")

        linha = pedir_numero("Linha (1-9): ", 1, 9) -1
        coluna =  pedir_numero("Coluna (1-9): ", 1, 9) -1
        numero = pedir_numero("Número (1-9): ", 1, 9)

        if fixos[linha][coluna]:
            print("Posição fixa!")
            print("Voce nao pode alterar essa posicao")

            continue


        if numero == solucao[linha][coluna]:
            tabuleiro[linha][coluna] = numero
            fixos[linha][coluna] = True
            print("Numero correto")
            
            if venceu(tabuleiro, solucao):
                mostrar(tabuleiro)
                print("\nPARABENS")
                return "venceu"
        else:
            print("Numero errado, bobao")



# ACHO Q É O PROGRAMA PRINCIPAL
menu()
