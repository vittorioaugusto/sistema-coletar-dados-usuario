import re, requests
from datetime import datetime
from dados import (
    USUARIOS,
    PROFISSOES,
    PROFISSOES_PROGRAMACAO,
    LINGUAGENS_PROGRAMACAO,
    DIAS_SEMANA,
    MESES,
)

data_hora_atual = datetime.now()

data_ptbr = data_hora_atual.strftime("%d/%m/%Y")
hora_ptbr = data_hora_atual.strftime("%H:%M")
dia_ptbr = data_hora_atual.strftime("%d")
dia_semana_ptbr = DIAS_SEMANA[data_hora_atual.weekday()]
mes_ptbr = MESES[data_hora_atual.month]
ano_ptbr = data_hora_atual.strftime("%Y")


class Usuario:
    id = 1

    def __init__(
        self, cpf, nome, idade, genero, email, telefone, cep, profissao, linguagem=None
    ):
        self.id = Usuario.id
        Usuario.id += 1
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.email = email
        self.telefone = telefone
        self.cep = cep
        self.profissao = profissao
        self.linguagem = linguagem

    def exibir_dados(self):
        print(f"\n### Dados do Usuário ###")
        print(f"ID {self.id}")
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Gênero: {self.genero}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"CEP: {self.cep['cep']}")
        print(f"Rua: {self.cep['rua']}")
        print(f"Bairro: {self.cep['bairro']}")
        print(f"Cidade: {self.cep['cidade']}")
        print(f"Estado: {self.cep['estado']}")
        print(f"País: {self.cep['pais']}")
        print(f"Profissão: {self.profissao}")
        if self.linguagem:
            print(f"Linguagem de Programação: {self.linguagem}")
        print("\n")


class ColetarDadosUsuario:
    def __init__(self):
        self.usuarios = USUARIOS

    def validar_cpf(self, cpf):
        return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf) is not None

    def obter_cpf(self):
        while True:
            cpf = input("Por favor, insira seu CPF (formato: xxx.xxx.xxx-xx): ").strip()
            if cpf.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            if self.validar_cpf(cpf):
                return cpf
            else:
                print(
                    "CPF inválido. Certifique-se de que está no formato xxx.xxx.xxx-xx."
                )

    def obter_nome(self):
        while True:
            nome = input("Qual o seu nome? ").strip().title()
            if nome.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            elif not nome.isalpha():
                print("Nome inválido. Por favor, insira apenas letras.")
            else:
                return nome

    def obter_idade(self):
        while True:
            idade = input("Qual a sua idade? ")
            if idade.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            try:
                return int(idade)
            except ValueError:
                print("Idade inválida. Por favor, insira um número inteiro.")

    def obter_genero(self):
        while True:
            genero = (
                input("Qual é o seu gênero (Masculino/Feminino/Outro)? ")
                .strip()
                .title()
            )
            if genero.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None

            generos_map = {"Mas": "Masculino", "Fem": "Feminino", "Out": "Outro"}

            if genero in ["Masculino", "Feminino", "Outro"] or genero in generos_map:
                return generos_map.get(genero, genero)
            else:
                print(
                    "Entrada inválida. Por favor, insira 'Masculino', 'Feminino', 'Outro' ou as abreviações 'Mas', 'Fem', 'Out'."
                )

    def validar_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def obter_email(self):
        while True:
            email = input("Por favor, insira seu email: ").strip()
            if email.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            if self.validar_email(email):
                return email
            else:
                print("Email inválido. Tente novamente.")

    def validar_telefone(self, telefone):
        return re.match(r"^\(?\d{2}\)?\s?\d{4,5}-\d{4}$", telefone) is not None

    def obter_telefone(self):
        while True:
            telefone = input(
                "Por favor, insira seu telefone (formato: (xx) xxxxx-xxxx ou xxxx-xxxx): "
            ).strip()
            if telefone.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            if self.validar_telefone(telefone):
                return telefone
            else:
                print(
                    "Telefone inválido. Certifique-se de que está no formato correto."
                )

    def validar_cep(self, cep):
        return re.match(r"^\d{5}-\d{3}$", cep) is not None

    def obter_dados_cep(self, cep):
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

    def obter_cep(self):
        while True:
            cep = input("Por favor, insira seu CEP (formato: xxxxx-xxx): ").strip()
            if cep.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            if self.validar_cep(cep):
                dados_cep = self.obter_dados_cep(cep)
                if dados_cep:
                    print(f"\nRua: {dados_cep['rua']}")
                    print(f"Bairro: {dados_cep['bairro']}")
                    print(f"Cidade: {dados_cep['cidade']}")
                    print(f"Estado: {dados_cep['estado']}")
                    print(f"País: {dados_cep['pais']}")
                    return dados_cep
            else:
                print("CEP inválido. Certifique-se de que está no formato xxxxx-xxx.")

    def obter_profissao(self):
        while True:
            profissao = input("\nQual a sua profissão? ").strip().lower()
            if profissao.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            todas_profissoes = [
                p.lower()
                for p in (
                    PROFISSOES
                    + PROFISSOES_PROGRAMACAO
                    + ["Desempregado", "Estudante", "Aposentado"]
                )
            ]

            if profissao in todas_profissoes:
                for p in (
                    PROFISSOES
                    + PROFISSOES_PROGRAMACAO
                    + ["Desempregado", "Estudante", "Aposentado"]
                ):
                    if p.lower() == profissao:
                        return p
            else:
                print("\nProfissões disponíveis: ")
                for profissao_disponivel in PROFISSOES + PROFISSOES_PROGRAMACAO:
                    print(f"- {profissao_disponivel}")
                profissao = (
                    input(
                        "Caso não tenha uma profissão, selecionar 'Desempregado', 'Estudante' ou 'Aposentado' "
                    )
                    .strip()
                    .lower()
                )
                if profissao in ["desempregado", "estudante", "aposentado"]:
                    return profissao.title()

    def obter_linguagem(self):
        while True:
            print("Linguagens de programação disponíveis:")
            for linguagem in LINGUAGENS_PROGRAMACAO:
                print(f"- {linguagem}")
            linguagem = input("\nQual a sua linguagem de programação? ").strip().title()
            if linguagem.lower() == "s":
                print("Cadastro de usuário cancelado.\n")
                return None
            if linguagem in [linguagem.title() for linguagem in LINGUAGENS_PROGRAMACAO]:
                return linguagem
            else:
                print(
                    "\nLinguagem não encontrada. Por favor, escolha uma das opções disponíveis."
                )

    def cadastrar_usuario(self):
        cpf = self.obter_cpf()
        if cpf is None:
            return

        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("\nErro: Usuário com este CPF já cadastrado.")
                return

        nome = self.obter_nome()
        if nome is None:
            return

        idade = self.obter_idade()
        if idade is None:
            return

        genero = self.obter_genero()
        if genero is None:
            return

        email = self.obter_email()
        if email is None:
            return

        telefone = self.obter_telefone()
        if telefone is None:
            return

        cep = self.obter_cep()
        if cep is None:
            return

        profissao = self.obter_profissao()
        if profissao is None:
            return

        linguagem = None
        if profissao in PROFISSOES_PROGRAMACAO:
            linguagem = self.obter_linguagem()
            if linguagem is None:
                return

        usuario = Usuario(
            cpf, nome, idade, genero, email, telefone, cep, profissao, linguagem
        )
        self.usuarios.append(usuario)
        print("\nUsuário cadastrado com sucesso!\n")

    def listar_usuarios(self):
        if not self.usuarios:
            print("\nNenhum usuário cadastrado.\n")
        else:
            for usuario in self.usuarios:
                usuario.exibir_dados()

    def consultar_usuario(self):
        cpf = self.obter_cpf()
        if cpf is None:
            return

        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario

        return None

    def editar_usuario(self):
        cpf = self.obter_cpf()
        if cpf is None:
            return

        usuario = None
        for u in self.usuarios:
            if u.cpf == cpf:
                usuario = u
                break

        if usuario is None:
            print("\nUsuário não encontrado.")
            return

        print(f"\nEditando dados do usuário: {usuario.nome}")

        while True:
            print("\nEscolha o dado que deseja editar:")
            print("[1] Nome")
            print("[2] Idade")
            print("[3] Gênero")
            print("[4] Email")
            print("[5] Telefone")
            print("[6] CEP")
            print("[7] Profissão")
            print("[8] Linguagem de Programação")
            print("[9] Cancelar edição")

            opcao = input("Digite o número da opção: ").strip()

            if opcao == "1":
                novo_nome = self.obter_nome()
                if novo_nome:
                    usuario.nome = novo_nome
                    print(f"\nNome atualizado para {usuario.nome}")

            elif opcao == "2":
                nova_idade = self.obter_idade()
                if nova_idade is not None:
                    usuario.idade = nova_idade
                    print(f"\nIdade atualizada para {usuario.idade} anos")

            elif opcao == "3":
                novo_genero = self.obter_genero()
                if novo_genero:
                    usuario.genero = novo_genero
                    print(f"\nGênero atualizado para {usuario.genero}")

            elif opcao == "4":
                novo_email = self.obter_email()
                if novo_email:
                    usuario.email = novo_email
                    print(f"\nEmail atualizado para {usuario.email}")

            elif opcao == "5":
                novo_telefone = self.obter_telefone()
                if novo_telefone:
                    usuario.telefone = novo_telefone
                    print(f"\nTelefone atualizado para {usuario.telefone}")

            elif opcao == "6":
                novo_cep = self.obter_cep()
                if novo_cep:
                    usuario.cep = novo_cep
                    print(f"\nCEP atualizado.")

            elif opcao == "7":
                nova_profissao = self.obter_profissao()
                if nova_profissao:
                    usuario.profissao = nova_profissao
                    if nova_profissao in PROFISSOES_PROGRAMACAO:
                        nova_linguagem = self.obter_linguagem()
                        if nova_linguagem:
                            usuario.linguagem = nova_linguagem
                    else:
                        usuario.linguagem = None
                    print(f"\nProfissão atualizada para {usuario.profissao}")

            elif opcao == "8":
                if usuario.profissao in PROFISSOES_PROGRAMACAO:
                    nova_linguagem = self.obter_linguagem()
                    if nova_linguagem:
                        usuario.linguagem = nova_linguagem
                        print(
                            f"\nLinguagem de Programação atualizada para {usuario.linguagem}"
                        )
                else:
                    print(
                        "\nEste usuário não tem uma profissão relacionada à programação."
                    )

            elif opcao == "9":
                print("Edição cancelada.")
                break

            else:
                print("Opção inválida. Tente novamente.")

    def excluir_usuario(self):
        cpf = self.obter_cpf()
        if cpf is None:
            return

        usuario_a_remover = None
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                usuario_a_remover = usuario
                break

        if usuario_a_remover:
            confirmacao = (
                input(
                    f"Tem certeza que deseja excluir o usuário {usuario_a_remover.nome}? (s/n): "
                )
                .strip()
                .lower()
            )
            if confirmacao == "s":
                self.usuarios.remove(usuario_a_remover)
                print(f"\nUsuário {usuario_a_remover.nome} foi excluído com sucesso!\n")
            else:
                print("\nExclusão cancelada.")
        else:
            print("\nUsuário não encontrado.\n")

    def menu_principal(self):
        while True:
            print(" Bem vindo ao Sistema Coletar Dados ".center(50, "#"))
            print(f"{dia_semana_ptbr} - {data_ptbr} - {hora_ptbr} ")
            print("[1] Cadastrar Usuário")
            print("[2] Consultar Usuário pelo CPF")
            print("[3] Listar Todos os Usuários Cadastrados")
            print("[4] Editar Usuário")
            print("[5] Excluir Usuário")
            print("[6] Sair do Sistema")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                print("Você selecionou: Cadastrar Usuário")
                self.cadastrar_usuario()
            elif opcao == "2":
                print("Você selecionou: Consultar Usuário pelo CPF")
                usuario = self.consultar_usuario()
                if usuario:
                    usuario.exibir_dados()
                else:
                    print("\nUsuário não encontrado.\n")
            elif opcao == "3":
                print("Você selecionou: Listar Todos os Usuários Cadastrados")
                self.listar_usuarios()
            elif opcao == "4":
                print("Você selecionou: Editar Usuário")
                self.editar_usuario()
            elif opcao == "5":
                print("Você selecionou: Excluir Usuário")
                self.excluir_usuario()
            elif opcao == "6":
                print("\nSaindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")


sistema = ColetarDadosUsuario()
sistema.menu_principal()
