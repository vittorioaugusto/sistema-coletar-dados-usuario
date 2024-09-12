import re, requests
from dados import (
    USUARIOS,
    PROFISSOES,
    PROFISSOES_PROGRAMACAO,
    LINGUAGENS_PROGRAMACAO,
)

id = 1


def validar_cpf(cpf):
    return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf) is not None


def obter_cpf():
    while True:
        cpf = input("Por favor, insira seu CPF (formato: xxx.xxx.xxx-xx): ").strip()
        if validar_cpf(cpf):
            return cpf
        else:
            print("CPF inválido. Certifique-se de que está no formato xxx.xxx.xxx-xx.")


def obter_nome():
    nome = input("Qual o seu nome? ").strip().title()
    while not nome.isalpha():
        nome = input("Nome inválido. Por favor, insira apenas letras: ").strip().title()
    return nome


def obter_idade():
    while True:
        try:
            idade = int(input("Qual a sua idade? "))
            return idade
        except ValueError:
            print("Idade inválida. Por favor, insira um número inteiro.")


def validar_telefone(telefone):
    return re.match(r"^\(?\d{2}\)?\s?\d{4,5}-\d{4}$", telefone) is not None


def obter_telefone():
    while True:
        telefone = input(
            "Por favor, insira seu telefone (formato: (xx) xxxxx-xxxx ou xxxx-xxxx): "
        ).strip()
        if validar_telefone(telefone):
            return telefone
        else:
            print("Telefone inválido. Certifique-se de que está no formato correto.")


def validar_cep(cep):
    return re.match(r"^\d{5}-\d{3}$", cep) is not None


def obter_dados_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if "erro" in dados:
            print("CEP não encontrado. Por favor, insira um CEP válido.")
            return None
        else:
            return {
                "cep": cep,
                "rua": dados.get("logradouro"),
                "bairro": dados.get("bairro"),
                "cidade": dados.get("localidade"),
                "estado": dados.get("uf"),
                "pais": "Brasil",
            }
    else:
        print("Erro ao consultar o CEP. Tente novamente.")
        return None


def obter_cep():
    while True:
        cep = input("Por favor, insira seu CEP (formato: xxxxx-xxx): ").strip()
        if validar_cep(cep):
            dados_cep = obter_dados_cep(cep)
            if dados_cep:
                print(f"\nRua: {dados_cep['rua']}")
                print(f"Bairro: {dados_cep['bairro']}")
                print(f"Cidade: {dados_cep['cidade']}")
                print(f"Estado: {dados_cep['estado']}")
                print(f"País: {dados_cep['pais']}")
                return dados_cep
        else:
            print("CEP inválido. Certifique-se de que está no formato xxxxx-xxx.")


def obter_profissao():
    while True:
        profissao = input("\nQual a sua profissão? ").strip().title()
        if profissao in PROFISSOES + PROFISSOES_PROGRAMACAO + [
            "Desempregado",
            "Estudante",
            "Aposentado",
        ]:
            return profissao
        else:
            print("\nProfissões disponíveis: ")
            for profissao in PROFISSOES + PROFISSOES_PROGRAMACAO:
                print(f"- {profissao}")
            profissao = (
                input(
                    "Caso não tenha uma profissão, selecionar 'Desempregado', 'Estudante' ou 'Aposentado' "
                )
                .strip()
                .title()
            )
            if (
                profissao
                in ["Desempregado", "Estudante", "Aposentado"]
                + PROFISSOES
                + PROFISSOES_PROGRAMACAO
            ):
                return profissao


def obter_linguagem():
    while True:
        print("Linguagens de programação disponíveis:")
        for linguagem in LINGUAGENS_PROGRAMACAO:
            print(f"- {linguagem}")
        linguagem = input("\nQual a sua linguagem de programação? ").strip().title()
        if linguagem in [linguagem.title() for linguagem in LINGUAGENS_PROGRAMACAO]:
            return linguagem
        else:
            print(
                "\nLinguagem de programação inválida. Por favor, escolha uma das linguagens listadas acima.\n"
            )


def dados_usuario(cpf):
    global id
    nome = obter_nome()
    idade = obter_idade()
    telefone = obter_telefone()
    cep = obter_cep()
    profissao = obter_profissao()

    if profissao in PROFISSOES_PROGRAMACAO:
        linguagem = obter_linguagem()
    else:
        linguagem = None

    usuario = {
        "id": id,
        "cpf": cpf,
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "cep": cep,
        "profissao": profissao,
        "linguagem": linguagem,
    }
    id += 1
    return usuario


def cadastrar_usuario():
    cpf = obter_cpf()
    for usuario in USUARIOS:
        if usuario["cpf"] == cpf:
            print("\nCPF já cadastrado. Tente novamente com um CPF diferente.")
            return

    usuario = dados_usuario(cpf)
    USUARIOS.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")


def consultar_usuario():
    cpf = obter_cpf()
    for usuario in USUARIOS:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def listar_usuarios():
    if not USUARIOS:
        print("\nNenhum usuário cadastrado.")
    else:
        for usuario in USUARIOS:
            print(f"\n### Dados do Usuário ###")
            print(f'ID {usuario['id']}')
            print(f"CPF: {usuario['cpf']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']} anos")
            print(f"Telefone: {usuario['telefone']}")
            print(f"CEP: {usuario['cep']['cep']}")
            print(f"Rua: {usuario['cep']['rua']}")
            print(f"Bairro: {usuario['cep']['bairro']}")
            print(f"Cidade: {usuario['cep']['cidade']}")
            print(f"Estado: {usuario['cep']['estado']}")
            print(f"País: {usuario['cep']['pais']}")
            print(f"Profissão: {usuario['profissao']}")
            if usuario["linguagem"]:
                print(f"Linguagem de Programação: {usuario['linguagem']}")
            print("\n")


menu = " Bem vindo ao Sistema Coletar Dados "


def main():
    while True:
        print(menu.center(50, "#"))
        print("[1] Cadastrar Usuário")
        print("[2] Consultar Usuário")
        print("[3] Listar Todos os Usuários Cadastrados")
        print("[4] Sair do Sistema")
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = consultar_usuario()
            if usuario:
                print(f"\n### Dados do Usuário ###")
                print(f"CPF: {usuario['cpf']}")
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']} anos")
                print(f"Telefone: {usuario['telefone']}")
                print(f"CEP: {usuario['cep']['cep']}")
                print(f"Rua: {usuario['cep']['rua']}")
                print(f"Bairro: {usuario['cep']['bairro']}")
                print(f"Cidade: {usuario['cep']['cidade']}")
                print(f"Estado: {usuario['cep']['estado']}")
                print(f"País: {usuario['cep']['pais']}")
                print(f"Profissão: {usuario['profissao']}")
                if usuario["linguagem"]:
                    print(f"Linguagem de Programação: {usuario['linguagem']}")
            else:
                print("\nUsuário não encontrado.\n")
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
