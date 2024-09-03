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
    nome = obter_nome()
    idade = obter_idade()
    moradia = obter_moradia()
    profissao = obter_profissao()

    if profissao in PROFISSOES_PROGRAMACAO:
        linguagem = obter_linguagem()
    else:
        linguagem = None

    return nome, idade, moradia, profissao, linguagem


def main():
    nome, idade, moradia, profissao, linguagem = dados_usuario()

    if profissao in ["Desempregado", "Aposentado"]:
        mensagem_profissao = f"estou {profissao}"
    elif profissao in ["Estudante"]:
        mensagem_profissao = f"sou {profissao}"
    else:
        mensagem_profissao = f"trabalho como {profissao}"

    mensagem = f"Olá, me chamo {nome}. Eu tenho {idade} anos, moro em {moradia} e {mensagem_profissao}."

    if linguagem:
        mensagem += f" Minha linguagem de programação favorita é {linguagem}."

    print(mensagem)


if __name__ == "__main__":
    main()
