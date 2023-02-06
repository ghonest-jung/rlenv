import pytest

from gridtsp import GridTSP


def test1():
    env = GridTSP((3, 3), max_num_tasks=1)
    env.reset(start=(0, 0), tasks=[(2, 2)])
    assert env.board[0][0] == 1
    assert env.board[1][0] == 0
    assert env.board[2][2] == 2

    assert env.sample_action() == [GridTSP.DOWN, GridTSP.RIGHT]

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][0] == 0
    assert env.board[0][0] == 0
    assert board[0][1] == 1
    assert env.board[0][1] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (0, 1)

    board, reward, done, info = env.step(GridTSP.LEFT)

    assert board[0][1] == 0
    assert env.board[0][1] == 0
    assert board[0][0] == 1
    assert env.board[0][0] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (0, 0)

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert board[0][0] == 0
    assert env.board[0][0] == 0
    assert board[1][0] == 1
    assert env.board[1][0] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (1, 0)

    board, reward, done, info = env.step(GridTSP.UP)

    assert board[1][0] == 0
    assert env.board[1][0] == 0
    assert board[0][0] == 1
    assert env.board[0][0] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (0, 0)

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][0] == 0
    assert env.board[0][0] == 0
    assert board[0][1] == 1
    assert env.board[0][1] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (0, 1)

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][1] == 0
    assert env.board[0][1] == 0
    assert board[0][2] == 1
    assert env.board[0][2] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (0, 2)

    assert env.sample_action() == [GridTSP.DOWN, GridTSP.LEFT]

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][2] == 1
    assert env.board[0][2] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (0, 2)

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert board[0][2] == 0
    assert env.board[0][2] == 0
    assert board[1][2] == 1
    assert env.board[1][2] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0
    assert info['location'] == (1, 2)

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert board[1][2] == 0
    assert env.board[1][2] == 0
    assert board[2][2] == 1
    assert env.board[2][2] == 1
    assert reward == 1
    assert done is True
    assert info['num_done_tasks'] == 1
    assert info['location'] == (2, 2)

    assert env.sample_action() == [GridTSP.UP, GridTSP.LEFT]


def test2():
    env = GridTSP((3, 3), max_num_tasks=2)
    env.reset(start=(0, 0), tasks=[(1, 0), (2, 2)])

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert reward == 1
    assert done is False
    assert info['num_done_tasks'] == 1

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 1

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 1

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert reward == 1
    assert done is True
    assert info['num_done_tasks'] == 2


def test3():
    env = GridTSP((3, 3), max_num_tasks=2)
    env.reset(start=(2, 1), tasks=[(1, 0), (2, 2)])

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert reward == 1
    assert done is False
    assert info['num_done_tasks'] == 1

    board, reward, done, info = env.step(GridTSP.LEFT)

    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 1

    board, reward, done, info = env.step(GridTSP.LEFT)

    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 1

    assert env.sample_action() == [GridTSP.UP, GridTSP.RIGHT]

    board, reward, done, info = env.step(GridTSP.UP)

    assert reward == 1
    assert done is True
    assert info['num_done_tasks'] == 2

    assert env.sample_action() == [GridTSP.UP, GridTSP.DOWN, GridTSP.RIGHT]


def test4():
    env = GridTSP((3, 3), max_num_tasks=2)
    env.reset(seed=0)

    assert len(env.tasks) <= env.max_num_tasks
