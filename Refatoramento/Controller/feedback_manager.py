class FeedbackManager:
    def __init__(self):
        self._feedbacks = []

    @property
    def feedbacks(self):
        return self._feedbacks

    def give_feedback(self):
        name = input("Nome do treino avaliado: ").strip()
        rating = input("Dê uma nota (1 a 5): ").strip()
        comment = input("Deixe um comentário: ").strip()
        if name and rating.isdigit() and 1 <= int(rating) <= 5:
            self._feedbacks.append({"Treino": name, "Nota": int(rating), "Comentário": comment})
            print("Obrigado pelo feedback!")
        else:
            print("Erro: Dados inválidos!")
    
    def see_feedback(self):
        if self._feedbacks:
            print("Seus feedbacks:")
            for feedback in self._feedbacks:
                print(f"Treino: {feedback['Treino']}, Nota: {feedback['Nota']}, Comentário: {feedback['Comentário']}.\n")
        else:
            print("Nenhum feedback encontrado!\n")