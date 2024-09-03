CIDADES = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Salvador",
    "Fortaleza",
    "Brasília",
    "Curitiba",
    "Manaus",
    "Recife",
    "Porto Alegre",
    "Belém",
    "Goiânia",
    "João Pessoa",
]

PROFISSOES = [
    "Autônomo",
    "Estagiário",
    "Jovem Aprendiz",
    "Freelancer",
    "Empreendedor",
    "Voluntário",
    "Pensionista",
    "Freelancer Júnior",
    "Profissional Liberal",
    "Trabalhador Informal",
    "Freelancer Pleno",
    "Freelance Part-Time",
    "Professor",
    "Engenheiro Civil",
    "Enfermeiro",
    "Advogado",
    "Agricultor",
    "Médico",
    "Enfermeiro",
    "Fisioterapeuta",
    "Dentista",
    "Psicólogo",
    "Nutricionista",
    "Farmacêutico",
    "Biomédico",
    "Fonoaudiólogo",
    "Veterinário",
]

PROFISSOES_PROGRAMACAO = [
    "Programador",
    "Desenvolvedor Front-End",
    "Desenvolvedor Back-End",
    "Desenvolvedor Full-Stack",
    "Engenheiro de Software",
    "Analista de Sistemas",
    "Desenvolvedor de Aplicativos",
    "Cientista de Dados",
    "Engenheiro de Dados",
    "Desenvolvedor de Jogos",
    "Arquiteto de Software",
    "Desenvolvedor Mobile",
    "Desenvolvedor Web",
    "Engenheiro de Machine Learning",
    "Engenheiro de Inteligência Artificial",
    "DevOps",
    "Desenvolvedor de Firmware",
    "Desenvolvedor de Banco de Dados",
    "Engenheiro de Automação",
    "Analista de Segurança da Informação",
    "Desenvolvedor de Sistemas Embarcados",
    "Engenheiro de Cloud",
    "Engenheiro de Rede",
]


def obter_nome():
    nome = input("Qual o seu nome? ").strip().title()
    while not nome:
        nome = input("Nome não pode ser vazio. Por favor, insira seu nome: ").strip()
    return nome


def obter_idade():
    while True:
        try:
            idade = int(input("Qual a sua idade? "))
            return idade
        except ValueError:
            print("Idade inválida. Por favor, insira um número inteiro.")


def obter_moradia():
    while True:
        moradia = input("Qual a cidade que você mora? ").strip().title()
        if moradia in [moradia.title() for moradia in CIDADES]:
            return moradia
        else:
            print("Cidade inválida. Por favor, escolha uma das seguintes opções: ")
            print(", ".join(CIDADES))


def obter_profissao():
    while True:
        profissao = input("Qual a sua profissão? ").strip().title()
        if profissao in PROFISSOES + PROFISSOES_PROGRAMACAO:
            return profissao
        else:
            print("Profissão inválida. Por favor, escolha uma das seguintes opções: ")
            print(", ".join(PROFISSOES + PROFISSOES_PROGRAMACAO))
            profissao = (
                input(
                    "Caso não tenha uma profissão, selecionar 'Desempregado', 'Estudante' ou 'Aposentado' "
                )
                .strip()
                .title()
            )
            if profissao in ["Desempregado", "Estudante", "Aposentado"]:
                return profissao


def dados_usuario():
    nome = obter_nome()
    idade = obter_idade()
    moradia = obter_moradia()
    profissao = obter_profissao()
    return nome, idade, moradia, profissao


def main():
    nome, idade, moradia, profissao = dados_usuario()

    if profissao in ["Desempregado", "Aposentado"]:
        mensagem_profissao = f"estou {profissao}"
    elif profissao in ["Estudante"]:
        mensagem_profissao = f"sou {profissao}"
    else:
        mensagem_profissao = f"trabalho como {profissao}"

    mensagem = f"Olá, me chamo {nome}. Eu tenho {idade} anos, moro em {moradia} e {mensagem_profissao}."

    print(mensagem)


if __name__ == "__main__":
    main()
