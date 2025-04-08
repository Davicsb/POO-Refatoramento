class ForumManager:
    """Classe responsável pela interação com o fórum da comunidade."""
    def access_forum(self):
        """Permite ao usuário acessar e navegar pelo fórum."""
        print("\n1. Ver tópicos populares\n2. Criar um novo tópico")
        option = input("Escolha uma opção: ").strip()
        if option == '1':
            print("- Como manter a motivação nos treinos?\n- Dicas de alimentação saudável")
        elif option == '2':
            title = input("Título do seu tópico: ").strip()
            if title:
                print(f"Seu tópico '{title}' foi criado com sucesso!")
        else:
            print("Opção inválida.")