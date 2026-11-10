import os

ARQUIVO = "clientes_vip.txt"

def inicializar_arquivo():
    """Cria o ficheiro com 20 clientes VIP iniciais caso ainda não exista."""
    if not os.path.exists(ARQUIVO):
        dados_iniciais = [
            "101 - Ana Silva - Diamond",
            "102 - Bruno Souza - Gold",
            "103 - Carlos Oliveira - Platinum",
            "104 - Daniela Lima - Diamond",
            "105 - Eduardo Ferreira - Gold",
            "106 - Fernanda Costa - Platinum",
            "107 - Gabriel Santos - Diamond",
            "108 - Helena Rodrigues - Gold",
            "109 - Igor Almeida - Platinum",
            "110 - Juliana Pereira - Diamond",
            "111 - Lucas Carvalho - Gold",
            "112 - Mariana Gomes - Platinum",
            "113 - Nicolas Martins - Diamond",
            "114 - Olivia Barbosa - Gold",
            "115 - Pedro Ribeiro - Platinum",
            "116 - Rafaela Alves - Diamond",
            "117 - Samuel Monteiro - Gold",
            "118 - Tatiane Mendez - Platinum",
            "119 - Vinicius Rocha - Diamond",
            "120 - Yasmin Cardoso - Gold"
        ]
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for linha in dados_iniciais:
                f.write(f"{linha}\n")

def carregar_clientes():
    """Lê o ficheiro e devolve um dicionário com os clientes."""
    clientes = {}
    if not os.path.exists(ARQUIVO):
        return clientes
    
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                partes = linha.split(" - ")
                if len(partes) == 3:
                    cpf, nome, nivel = partes
                    clientes[cpf] = {"nome": nome, "nivel": nivel}
    return clientes

def salvar_clientes(clientes):
    """Guarda o dicionário de clientes no ficheiro .txt."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for cpf, dados in clientes.items():
            f.write(f"{cpf} - {dados['nome']} - {dados['nivel']}\n")

def cadastrar_cliente():
    clientes = carregar_clientes()
    print("\n--- CADASTRAR CLIENTE VIP ---")
    cpf = input("ID/CPF (ex: 121): ").strip()
    
    if cpf in clientes:
        print("❌ Erro: Já existe um cliente cadastrado com este ID/CPF.")
        return

    nome = input("Nome completo: ").strip()
    print("Níveis VIP disponíveis: [1] Gold  [2] Platinum  [3] Diamond")
    opcao_nivel = input("Escolha o nível (1/2/3): ").strip()
    
    niveis = {"1": "Gold", "2": "Platinum", "3": "Diamond"}
    nivel = niveis.get(opcao_nivel, "Gold")

    clientes[cpf] = {"nome": nome, "nivel": nivel}
    salvar_clientes(clientes)
    print(f"✅ Cliente {nome} (VIP {nivel}) cadastrado com sucesso!")

def listar_clientes():
    clientes = carregar_clientes()
    print("\n--- LISTA DE CLIENTES VIP ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    for cpf, dados in clientes.items():
        print(f"ID/CPF: {cpf} | Nome: {dados['nome']} | Nível VIP: {dados['nivel']}")

def buscar_cliente():
    clientes = carregar_clientes()
    print("\n--- BUSCAR CLIENTE VIP ---")
    cpf = input("Digite o ID/CPF do cliente: ").strip()
    
    cliente = clientes.get(cpf)
    if cliente:
        print(f"\n✅ Cliente Encontrado:")
        print(f"Nome: {cliente['nome']}\nNível VIP: {cliente['nivel']}")
    else:
        print("❌ Cliente não encontrado.")

def remover_cliente():
    clientes = carregar_clientes()
    print("\n--- REMOVER CLIENTE VIP ---")
    cpf = input("Digite o ID/CPF do cliente a remover: ").strip()
    
    if cpf in clientes:
        nome = clientes[cpf]["nome"]
        del clientes[cpf]
        salvar_clientes(clientes)
        print(f"✅ Cliente {nome} removido com sucesso!")
    else:
        print("❌ Cliente não encontrado.")

def menu():
    # Cria o ficheiro com 20 registos assim que o programa arranca
    inicializar_arquivo()
    
    while True:
        print("\n=== SISTEMA DE GESTÃO CLIENTE VIP ===")
        print("1. Cadastrar Cliente VIP")
        print("2. Listar Todos os VIPs")
        print("3. Buscar VIP por ID/CPF")
        print("4. Remover Cliente VIP")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()