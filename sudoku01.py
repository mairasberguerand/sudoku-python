# IMPORTAÇÕES
import random



# CRIAÇÃO DO TABULEIRO
def criar_tabuleiro():
    tabuleiro = []

    for i in range(9):
        linha = []

        for j in range(9):
            linha.append(0)
        tabuleiro.append(linha)
    
    return tabuleiro

def mostrar(tabuleiro):
    print()
    print("     A B C   D E F   G H I")
    print("   ┌───────┬───────┬───────┐")

    for i in range(9):
        print(f"{i+1}  | ", end="")

        for j in range(9):
            if tabuleiro[i][j] == 0:
                print("·", end=" ")
            else:
                print(tabuleiro[i][j], end=" ")
                    
            if (j + 1) % 3 == 0 and j != 8:
                print("| ", end="")

        print("|")
        if i == 2 or i == 5:
            print("   ├───────┼───────┼───────┤")

    print("   └───────┴───────┴───────┘")



# VALIDAÇÕES
def pode_colocar(tabuleiro, linha, coluna, numero):
    
    for i in range(9): # Verifica se o número já existe na linha.
        if tabuleiro[linha][i] == numero:
            return False
            
    for i in range(9): # Verifica se o número já existe na coluna.
        if tabuleiro[i][coluna] == numero:
            return False
            
    # Verifica o bloco 3x3 correspondente.
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if tabuleiro[i][j] == numero:
                return False
                
    return True

def encontrar_vazio(tabuleiro):
    
    for linha in range(9):
        for coluna in range(9):
            
            if tabuleiro[linha][coluna] == 0:
                return (linha, coluna)
    return None



# GERAÇÃO DO SUDOKU
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

def remover_numeros(tabuleiro, quantidade):
    while quantidade > 0:

        linha = random.randint(0,8)
        coluna = random.randint(0,8)

        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            quantidade -= 1

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



# ENTRADA DE DADOS
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

def escolher_dificuldade():
    print("\nEscolha a dificuldade")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    return pedir_numero("Opção: ", 1, 3)

def ler_coordenada():
    while True:
        coordenada = input("Casa: ").strip().upper()

        if len(coordenada) != 2:
            print("Digite uma coordenada válida. Exemplo: A1")
            continue

        letra = coordenada[0]
        numero = coordenada[1]

        if letra < "A" or letra > "I":
            print("A coluna deve ser uma letra entre A e I.")
            continue

        if numero < "1" or numero > "9":
            print("A linha deve ser um número entre 1 e 9")
            continue

        coluna = ord(letra) - ord("A")
        linha = int(numero) - 1

        return linha, coluna

def ler_numero():
    while True:
        entrada = input("Número (1-9 X para apagar): ").strip().upper()

        if entrada == "X":
            return "X"

        if entrada.isdigit():
            numero = int(entrada)

            if 1 <= numero <= 9:
                return numero

        print("Digite um número entre 1 e 9, ou X.")

def pausar():
    input("\nPressione ENTER para continuar...")



# JOGO
def venceu(tabuleiro, solucao):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] != solucao[linha][coluna]:
                return False
    return True

def nome_dificuldade(dificuldade):
    if dificuldade == 1:
        return "Fácil"

    elif dificuldade == 2:
        return "Médio"

    else:
        return "Difícil"

def cabecalho(dificuldade):
    print("\n====================================")
    print("              S U D O K U")
    print("====================================")
    print(f"Dificuldade: {nome_dificuldade(dificuldade)}")
    print("====================================\n")

def jogar(tabuleiro, solucao, fixos, dificuldade):

    while True:
        cabecalho(dificuldade)
        mostrar(tabuleiro)

        print("\nDigite a sua jogada:")

        linha, coluna = ler_coordenada()
        numero = ler_numero()

        if fixos[linha][coluna]:
            print("⚠ Posição fixa!")
            print("Escolha outra casa.")
            pausar()
            continue

        if numero == "X":
            tabuleiro[linha][coluna] = 0
            fixos[linha][coluna] = False
            print("✓ Número removido.")
            pausar()
            continue

        if numero == solucao[linha][coluna]:
            tabuleiro[linha][coluna] = numero
            fixos[linha][coluna] = True
            print("✓ Número correto!")
            
            if venceu(tabuleiro, solucao):
                cabecalho(dificuldade)
                mostrar(tabuleiro)

                print("====================================")
                print("        🎉 PARABÉNS! 🎉")
                print()
                print(f"Sudoku {nome_dificuldade(dificuldade)} concluído!")
                print("====================================")
                return "venceu"
        else:
            print("✗ Número incorreto.")
            pausar()

def menu():
    while True:
        print("\n====================================")
        print("            S U D O K U")
        print("====================================")
        print()
        print("1. Novo jogo")
        print("2. Como jogar")
        print("3. Sair")
        print()
        print("====================================")

        opcao = pedir_numero("Escolha uma opção: ", 1, 3)

        if opcao == 1:
            dificuldade = escolher_dificuldade()

            while True:

                tabuleiro, solucao, fixos = novo_jogo(dificuldade)
                jogar(tabuleiro, solucao, fixos, dificuldade)

                print("\n==============================")
                print("          FIM DA PARTIDA")
                print("====================================")
                print("1 - Jogar novamente")
                print("2 - Voltar ao menu")
                print("3 - Sair")
                print("====================================")

                escolha = pedir_numero("Opcao: ", 1 ,3)

                if escolha == 1:
                    dificuldade = escolher_dificuldade()
                    continue
                elif escolha == 2:
                    break
                elif escolha == 3:
                    return

        elif opcao == 2:
            print("\n========== COMO JOGAR ==========")
            print("O objetivo é preencher todas as casas vazias.")
            print()
            print("Regras:")
            print()
            print("• Cada linha deve conter os números de 1 a 9.")
            print("• Cada coluna deve conter os números de 1 a 9.")
            print("• Cada bloco 3x3 também.")
            print()
            print("Coordenadas:")
            print("A1, C5, H9...")
            print()
            print("Digite X para apagar um número.")
            print()
            print("Boa sorte!")
            input("\nPressione ENTER para voltar ao menu.")

        elif opcao == 3:
            print("\nByebye")
            break



menu()