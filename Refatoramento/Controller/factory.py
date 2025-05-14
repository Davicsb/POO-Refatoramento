from Controller.facade import FitnessComponentFactory

class Factory:
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
        if self.activity_tracker.progress["Passos"] < self.activity_tracker.goals["Passos"] * 0.5:
            print("- Caminhe mais para atingir sua meta!")
        else:
            print("Você está indo bem, atingiu sua meta de passos, continue assim!")
        if self.activity_tracker.progress["Calorias"] < self.activity_tracker.goals["Calorias"] * 0.5:
            print("- Considere um treino aeróbico para queimar mais calorias.")
        else:
            print("Você está indo bem, atingiu sua meta de calorias, continue assim!")
            
    def see_data(self):
        self.feedback_manager.see_feedback()
        self.workout_manager.see_workout()
        self.activity_tracker.check_progress()