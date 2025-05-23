class WorkoutManager:
    def __init__(self):
        self._workouts = []

    @property
    def workouts(self):
        return self._workouts

    def workout(self):
        option = input("1 - Criar treino\n2 - Ver treinos.\n")
        if option == '1':
            self.create_workout()
        elif option == '2':
            self.see_workout()
        else:
            print("Opção inválida!")
        
    def create_workout(self):
        name = input("Nome do treino: ").strip()
        description = input("Descrição do treino: ").strip()
        if name and description:
            self._workouts.append({"Nome": name, "Descrição": description})
            print("Treino adicionado com sucesso!")
        else:
            print("Erro: Nome e descrição não podem estar vazios.")
        
    def see_workout(self):
        if self._workouts:
            print("Seus treinos:")
            for workout in self._workouts:
                print(f"Treino: {workout['Nome']}, Descrição: {workout['Descrição']}.\n")
        else:
            print("Nenhum treino encontrado!")
            
    def execute(self):
        self.workout()