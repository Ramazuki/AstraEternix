from src.gameobjects.rocket import Rocket


class RocketScreen(Rocket):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def get_rocket(self):
        s = []
        for row in self.cur_rocket:
            s.append(row)
        return s
