import time
from Controller.factory import Factory
from Models.adapter import GoalSetter, DeviceSyncer, ShareProgressAdapter, RecommendationsAdapter, DataViewer, ExitHandler

class FitnessApp:
    def __init__(self):
        self.factory = Factory()
        
    def display_menu(self):
        print("\nBem-vindo(a) ao Fitness App!\nO que você deseja fazer hoje?\n")
        options = [
            "1. Criar/Gerenciar Plano de Treino",
            "2. Rastrear Atividades",
            "3. Rastrear Nutrição e Dieta",
            "4. Definir Metas e Acompanhar Progresso",
            "5. Sincronizar Dispositivo Vestível",
            "6. Compartilhar Progresso e Participar de Desafios",
            "7. Acessar Tutoriais e Guias em Vídeo",
            "8. Obter Recomendações Personalizadas",
            "9. Avaliar e Dar Feedback",
            "10. Acessar Fórum da Comunidade",
            "11. Exibir Dados",
            "12. Sair"
        ]
        for option in options:
            print(option)
        return input("\nEscolha uma opção: ").strip()

    def run(self):
        functions = {
            "1": self.factory.workout_manager,
            "2": self.factory.activity_tracker,
            "3": self.factory.nutrition_tracker,
            "4": GoalSetter(self.factory.activity_tracker),
            "5": DeviceSyncer(self.factory.activity_tracker),
            "6": ShareProgressAdapter(self.factory),
            "7": self.factory.tutorial_manager,
            "8": RecommendationsAdapter(self.factory),
            "9": self.factory.feedback_manager,
            "10": self.factory.forum_manager,
            "11": DataViewer(self.factory),
            "12": ExitHandler()
        }

        while True:
            option = self.display_menu()
            print()
            if option in functions:
                functions[option].execute()
            else:
                print("Opção inválida. Tente novamente.")
            time.sleep(1)