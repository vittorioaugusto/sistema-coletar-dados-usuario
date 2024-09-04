import re

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
    "Natal",
    "Maceió",
    "Teresina",
    "Campo Grande",
    "Cuiabá",
    "Aracaju",
    "São Luís",
    "Florianópolis",
    "Vitória",
    "Macapá",
    "Palmas",
    "Boa Vista",
    "Porto Velho",
    "Rio Branco",
    "Santos",
    "Campinas",
    "Sorocaba",
    "Niterói",
    "Caxias do Sul",
    "Londrina",
    "Maringá",
    "Joinville",
    "Blumenau",
    "Uberlândia",
    "Ribeirão Preto",
    "São José dos Campos",
    "Santo André",
    "Osasco",
    "Jundiaí",
    "Piracicaba",
    "Bauru",
    "São José do Rio Preto",
    "Mogi das Cruzes",
    "Volta Redonda",
    "Petrópolis",
    "Campos dos Goytacazes",
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

LINGUAGENS_PROGRAMACAO = [
    "Python",
    "Java",
    "C++",
    "PHP",
    "C",
    "C#",
    "JavaScript",
    "Ruby",
    "Go",
    "Swift",
    "Kotlin",
    "Rust",
    "TypeScript",
    "R",
    "Dart",
    "Scala",
    "Perl",
    "Haskell",
    "Lua",
    "Objective-C",
    "MATLAB",
    "Visual Basic",
    "Julia",
    "Elixir",
    "Erlang",
    "F#",
    "Scheme",
    "Prolog",
    "Assembly",
    "SQL",
    "Shell",
    "Groovy",
    "COBOL",
    "Fortran",
    "Ada",
    "Pascal",
    "VHDL",
    "Verilog",
    "SAS",
    "LabVIEW",
    "Lisp",
    "OCaml",
    "Scratch",
    "Smalltalk",
    "Tcl",
    "ABAP",
    "Delphi/Object Pascal",
    "Crystal",
    "Nim",
    "Solidity",
    "Zig",
    "Powershell",
]


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


def obter_moradia():
    while True:
        print("Cidades disponíveis: ")
        for numero, cidade in enumerate(CIDADES, start=1):
            print(f"{numero}. {cidade}")
        moradia = input("\nEm qual cidade você mora? ").strip().title()
        if moradia in CIDADES:
            return moradia
        else:
            print(
                "\nCidade inválida. Por favor, escolha uma das cidades listadas acima.\n"
            )


def obter_profissao():
    while True:
        profissao = input("Qual a sua profissão? ").strip().title()
        if profissao in PROFISSOES + PROFISSOES_PROGRAMACAO + [
            "Desempregado",
            "Estudante",
            "Aposentado",
        ]:
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


def obter_linguagem():
    while True:
        linguagem = input("Qual a sua linguagem de programação? ").strip().title()
        if linguagem in [linguagem.title() for linguagem in LINGUAGENS_PROGRAMACAO]:
            return linguagem
        else:
            print(
                "Linguagem de programação inválida. Por favor, escolha uma das seguintes opções: "
            )
            print(", ".join(LINGUAGENS_PROGRAMACAO))


def dados_usuario():
    cpf = obter_cpf()
    nome = obter_nome()
    idade = obter_idade()
    moradia = obter_moradia()
    profissao = obter_profissao()

    if profissao in PROFISSOES_PROGRAMACAO:
        linguagem = obter_linguagem()
    else:
        linguagem = None

    return cpf, nome, idade, moradia, profissao, linguagem


def main():
    cpf, nome, idade, moradia, profissao, linguagem = dados_usuario()

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
        f"Cidade: {moradia}\n"
        f"{mensagem_profissao}"
    )

    if linguagem:
        mensagem += f"\nLinguagem de Programação: {linguagem}"

    print(mensagem)


if __name__ == "__main__":
    main()
