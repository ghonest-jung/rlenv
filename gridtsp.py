import numpy as np


class GridTSP:
    STAY: int = 0
    UP: int = 1
    DOWN: int = 2
    LEFT: int = 3
    RIGHT: int = 4

    DELTA_R = [0, -1, 1, 0, 0]
    DELTA_C = [0, 0, 0, -1, 1]

    def __init__(self, size: tuple, start: tuple, tasks: list, reward_default: float = -0.01):
        self.size: tuple = size
        self.start: tuple = start
        self.tasks: list[tuple] = tasks
        self.reward_default: float = reward_default

        self.board = np.zeros(self.size, dtype=int)
        self.r: int = 0
        self.c: int = 0
        self.info: dict = {}

        self.reset()

    def reset(self):
        self.board = np.zeros(self.size, dtype=int)
        self.r = self.start[0]
        self.c = self.start[1]

        self.info = {
            "num_done_tasks": 0,
        }

        self.board[self.r][self.c] = 1
        for task in self.tasks:
            self.board[task[0]][task[1]] = 2

    def step(self, action):
        next_r = self.r + self.DELTA_R[action]
        next_c = self.c + self.DELTA_C[action]

        reward = self.reward_default
        done = False

        if 0 <= next_r < self.size[0] and 0 <= next_c < self.size[1]:
            self.board[self.r][self.c] = 0

            if self.board[next_r][next_c] == 2:
                self.info['num_done_tasks'] += 1
                reward = 1

            self.board[next_r][next_c] = 1
            self.r = next_r
            self.c = next_c

            if self.info['num_done_tasks'] == len(self.tasks):
                done = True

        return self.board, reward, done, self.info
