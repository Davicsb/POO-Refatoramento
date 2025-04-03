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