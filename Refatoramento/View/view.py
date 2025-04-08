import time
from Controller.factory import FitnessComponentFactory

class FitnessApp:
    def __init__(self, factory=None):
        self.factory = factory or FitnessComponentFactory()
        self._build_components()

    def _build_components(self):
        self.workout_manager = self.factory.create_workout_manager()
        self.activity_tracker = self.factory.create_activity_tracker()
        self.nutrition_tracker = self.factory.create_nutrition_tracker()
        self.feedback_manager = self.factory.create_feedback_manager()
        self.tutorial_manager = self.factory.create_tutorial_manager()
        self.forum_manager = self.factory.create_forum_manager()

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
            "1": self.workout_manager.create_workout,
            "2": self.activity_tracker.track,
            "3": self.nutrition_tracker.track,
            "4": self.activity_tracker.set_goals,
            "5": self.activity_tracker.device_sync,
            "6": self.share_progress,
            "7": self.tutorial_manager.access_tutorials,
            "8": self.get_recommendations,
            "9": self.feedback_manager.give_feedback,
            "10": self.forum_manager.access_forum,
            "11": self.see_data,
            "12": exit
        }
        while True:
            option = self.display_menu()
            print()
            if option in functions:
                functions[option]()
            else:
                print("Opção inválida. Tente novamente.")
            time.sleep(1)

    def share_progress(self):
        print("\n1. Compartilhar progresso\n2. Participar de um desafio")
        option = input("Escolha uma opção: ").strip()
        if option == '1':
            print("Seu progresso foi compartilhado!")
        elif option == '2':
            print("Você entrou em um desafio de 10.000 passos diários!")
        else:
            print("Opção inválida.")

    def get_recommendations(self):
        print("\nRecomendações Personalizadas:")
        if self.activity_tracker.progress["Passos"] < self.goal_manager.goals["Passos"] * 0.5:
            print("- Caminhe mais para atingir sua meta!")
        if self.activity_tracker.progress["Calorias"] < self.goal_manager.goals["Calorias"] * 0.5:
            print("- Considere um treino aeróbico para queimar mais calorias.")
            
    def see_data(self):
        self.feedback_manager.see_feedback()
        self.workout_manager.see_workout()
        self.activity_tracker.check_progress()