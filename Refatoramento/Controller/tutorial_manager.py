class TutorialManager:
    def __init__(self):
        self._videos = ["Treino para Iniciantes - link", "Treino Avançado - link"]

    @property
    def videos(self):
        return self._videos

    def access_tutorials(self):
        print("\nTutoriais e Guias em Vídeo:")
        for video in self._videos:
            print(video)