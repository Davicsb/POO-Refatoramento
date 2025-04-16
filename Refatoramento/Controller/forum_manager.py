class ForumManager:
    def __init__(self):
        self.forum = ["Como manter nos treinos"]

    """Classe responsável pela interação com o fórum da comunidade."""
    def access_forum(self):
        """Permite ao usuário acessar e navegar pelo fórum."""
        print("\n1. Ver tópicos populares\n2. Criar um novo tópico")
        option = input("Escolha uma opção: ").strip()
        
        if option == '1':
            print("\nTópicos do Fórum:")
            for i, topic in enumerate(self.forum, 1):
                print(f"{i}. {topic}")
        
        elif option == '2':
            title = input("Título do seu tópico: ").strip()
            if title:
                self.forum.append(title)
                print(f"Seu tópico '{title}' foi criado com sucesso!")
            else:
                print("Título inválido.")
        else:
            print("Opção inválida.")

    def execute(self):
        self.access_forum()