import os

produto = [{"codigo":"01","nome":"agua", "preco":"2.50" }]

def exibir_nome_do_programa():
    print("""
░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║
██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░

██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██╔══██╗██║░░██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║
██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║
██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░
""")

def exibir_opcoes():
    print(" 1. Cadastrar produto")
    print(" 2. Listar produtos")
    print(" 3. Sair \n")

def finalizar_app():
    exibir_subtitulo("\nFinalizado.\n \nObrigado por usar o sistema!\n")
    exit()

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao Menu: ")
    main()

def opcao_invalida():
    """Retorna mensagem e retorna ao menu"""
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Função responsável por limpar o terminal e apresentar texto selecionado com duas linhas de asteriscos em baixo e cima"""
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_produto():
    """Essa função é responsável por cadastrar um novo produto"""
    exibir_subtitulo("Cadastrar novo produto")
    codigo_do_produto = input("Digite o código do produto que deseja cadastrar: ")
    nome = str(input(f"Digite o nome do produto {codigo_do_produto}: "))
    preco = float(input(f"Digite o preço do produto {nome}: "))
    dados_do_produto = {"codigo": codigo_do_produto, "nome": nome, "preco": preco}
    produto.append(dados_do_produto)
    print(f"O produto {nome} foi cadastrado com sucesso! \n ")
    voltar_ao_menu_principal()

def listar_produtos():
    """Exibe a lista de produtos"""
    exibir_subtitulo("Listar produtos")
    print(f" {'Código'.ljust(10)} | {'Nome'.ljust(20)} | Preço")
    for prod in produto:
        codigo = prod["codigo"]
        nome = prod["nome"]
        preco = prod["preco"]
        
        print(f" {codigo.ljust(10)} | {nome.ljust(20)} | R${preco}")
    voltar_ao_menu_principal()

def escolher_opcao():

    while True:
        try:
            opcao_escolhida = int(input("Escolha uma opção: "))
            if opcao_escolhida == 1:
                cadastrar_novo_produto()
                break
            elif opcao_escolhida == 2:
                listar_produtos()
                break
            elif opcao_escolhida == 3:
                finalizar_app()
                break
            else:
                
                print("\nOpção inválida!\n")
                exibir_opcoes()
        except ValueError:
            exibir_opcoes()



def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
