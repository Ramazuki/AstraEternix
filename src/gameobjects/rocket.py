from src.gameobjects.stages import rocket, stages
from typing import List


class Rocket:
    def __init__(self):
        self.stage = 0
        self.cur_rocket: List[str] = [' ' * 16 for _ in range(13)]

    def get_rocket(self):
        return self.cur_rocket

    def next_stage(self):
        if self.stage >= 5:
            raise IndexError('Last stage was already approached')
        self.stage += 1
        for row in stages[self.stage - 1]:
            self.cur_rocket[row] = rocket[row]

    def __str__(self):
        s = ""
        for row in self.cur_rocket:
            s += row + "\n"
        return s


if __name__ == "__main__":
    r1 = Rocket()
    print(f'Rocket stage {r1.stage}', r1, sep="\n")
    r1.next_stage()
    print(f'Rocket stage {r1.stage}', r1, sep="\n")
    r1.next_stage()
    print(f'Rocket stage {r1.stage}', r1, sep="\n")
    r1.next_stage()
    print(f'Rocket stage {r1.stage}', r1, sep="\n")
    r1.next_stage()
    print(f'Rocket stage {r1.stage}', r1, sep="\n")
    r1.next_stage()
    print(f'Rocket stage {r1.stage}', r1, sep="\n")
