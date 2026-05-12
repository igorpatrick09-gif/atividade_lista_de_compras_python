print("ｍｅｒｃａｄｉｎｈｏ　ｐｒｅçｏ　ｔｏｐ")

print("Olá, seja bem vindo ao mercadinho preço top, boas compras!!")

lista = []

def exibir_menu():

    print("-==LISTA DE COMPRAS==-")
    print("1 - Adicionar Produto")
    print("2 - Visualizar Lista")
    print("3 - Remover Produto")
    print("4 - Sair")

while True:

    exibir_menu()

    opcao = int (input("Escolha uma opção:"))

    if opcao == 1:
        nome_produto = input("Informe o nome do produto:")
        lista.append(nome_produto)

    elif opcao == 2:
        print(lista)

    elif opcao == 3:
        nome_produto = input("Informe o nome do produto que deseja remover:")
        lista.remove(nome_produto)
        

    elif opcao == 4:
        break

    else:
        print("Opção Inválida")