import os

restaurantes=[{'nome':'Praça', 'categoria':'Japonesa','ativo':False},
              {'nome':'Pizza', 'categoria':'Pizzaria','ativo':True}]

def limpar_tela(string):
    os.system('cls')
    print(f'{string}  restaurante')

def tecla():
    input('Aperte ENTER para voltar ao menu principal ')
    main()


def listar_restaurantes():
    limpar_tela('Listando')

    for restaurante in restaurantes:
        print(f'{restaurante}')
    tecla()
    


def finalizar_app():
    os.system('cls')
    print("Encerrando...\n")

def exibir_nome():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def opcoes():


    print('1-Cadastrar Restaurante')
    print('2-Alterar estado de Restaurante')
    print('3-Ativar Restaurante')
    print('4-Sair')

def invalido():
    print("Opção inválida\n")
    tecla()

def cadastrar_novo():
    limpar_tela('Cadastrar')
    nome_restaurante=input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} foi cadastrado')
    tecla()

def alterar_estado():
    limpar_tela('Ativando')

    nome = input('Digite o nome do restaurante que deseja alterar o estado:')
    flag= False

    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            flag=True
            restaurante['ativo'] = not restaurante['ativo']
            print('Estado do restaurante foi alterado')
    if not flag:
        print('Restaurante não encontrado')

    tecla()


def escolher():
    try:

        opcao_escolhida = int(input('Escolha uma opção:'))
        print(f'Voce escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo()
        elif opcao_escolhida == 2:
            print('Listar restaurante')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
            alterar_estado()
        elif opcao_escolhida==4:
            finalizar_app()
        else:
            invalido()
    except:
        invalido()




def main():
    exibir_nome()
    opcoes()
    escolher()


if __name__ == '__main__':
    main()


