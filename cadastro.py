def cadastrar_nome(cadastro):
    novo_nome = input("Digite o nome da pessoa: ")
    cadastro.append(novo_nome)
    print(f"Usuário {novo_nome} foi adicionado com sucesso")

def lista_nomes(cadastro):
    print("\nLista de nomes cadastrados: ")
    for i, nome in enumerate(cadastro, start=1):
        print(f"{i}. {nome}")

def excluir_nomes(cadastro):
    excluir_nome = input("Digite o nome para excluir: ")
    if excluir_nome in cadastro:
        cadastro.remove(excluir_nome)
        print(f"{excluir_nome} foi removido.")
    else:
        print("Nome não encontrado.")

def menu():
    cadastro = []
    while True:
        print("\n-----Cadastro de funcionários-----")
        print("[1] Cadastrar pessoa")
        print("[2] Listar pessoas")
        print("[3] Excluir pessoa")
        print("[0] ")
        opção = input("Escolha uma opção: ")

        if opção == '1':
            cadastrar_nome(cadastro)
        elif opção == '2':
            lista_nomes(cadastro)
        elif opção =='3':
            excluir_nomes(cadastro)
        elif opção == '0':
            print("Saindo...")
            break
        else:
            print("!!! Opção inválida. Tente novamente. !!!")
menu()