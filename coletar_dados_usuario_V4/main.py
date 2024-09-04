import re
from dados import CIDADES, PROFISSOES, PROFISSOES_PROGRAMACAO, LINGUAGENS_PROGRAMACAO


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


def obter_cidade():
    while True:
        print("\nCidades disponíveis: ")
        for cidade in CIDADES:
            print(f"- {cidade}")
        cidade = input("\nEm qual cidade você mora? ").strip().title()
        if cidade in CIDADES:
            return cidade
        else:
            print(
                "\nCidade inválida. Por favor, escolha uma das cidades listadas acima.\n"
            )


def obter_profissao():
    while True:
        print("\nProfissões disponíveis: ")
        for profissao in PROFISSOES + PROFISSOES_PROGRAMACAO:
            print(f"- {profissao}")
        profissao = input("\nQual a sua profissão? ").strip().title()
        if profissao in PROFISSOES + PROFISSOES_PROGRAMACAO + [
            "Desempregado",
            "Estudante",
            "Aposentado",
        ]:
            return profissao
        else:
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


def dados_usuario():
    cpf = obter_cpf()
    nome = obter_nome()
    idade = obter_idade()
    telefone = obter_telefone()
    cidade = obter_cidade()
    profissao = obter_profissao()

    if profissao in PROFISSOES_PROGRAMACAO:
        linguagem = obter_linguagem()
    else:
        linguagem = None

    return cpf, nome, idade, telefone, cidade, profissao, linguagem


def main():
    cpf, nome, idade, telefone, cidade, profissao, linguagem = dados_usuario()

    if profissao in ["Desempregado", "Aposentado"]:
        mensagem_profissao = f"Status: {profissao}"
    elif profissao in ["Estudante"]:
        mensagem_profissao = f"Status: {profissao}"
    else:
        mensagem_profissao = f"Profissão: {profissao}"

    mensagem = (
        f"\n### Seus Dados ###\n"
        f"CPF: {cpf}\n"
        f"Nome: {nome}\n"
        f"Idade: {idade} anos\n"
        f"Telefone: {telefone}\n"
        f"Cidade: {cidade}\n"
        f"{mensagem_profissao}"
    )

    if linguagem:
        mensagem += f"\nLinguagem de Programação: {linguagem}"

    print(mensagem)


if __name__ == "__main__":
    main()
