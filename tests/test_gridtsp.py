import pytest

from gridtsp import GridTSP


def test1():
    env = GridTSP((3, 3), (0, 0), [(2, 2)])

    assert env.board[0][0] == 1
    assert env.board[1][0] == 0
    assert env.board[2][2] == 2

    board, reward, done, info = env.step(GridTSP.STAY)

    assert board[0][0] == 1
    assert env.board[0][0] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][0] == 0
    assert env.board[0][0] == 0
    assert board[0][1] == 1
    assert env.board[0][1] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.LEFT)

    assert board[0][1] == 0
    assert env.board[0][1] == 0
    assert board[0][0] == 1
    assert env.board[0][0] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert board[0][0] == 0
    assert env.board[0][0] == 0
    assert board[1][0] == 1
    assert env.board[1][0] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.UP)

    assert board[1][0] == 0
    assert env.board[1][0] == 0
    assert board[0][0] == 1
    assert env.board[0][0] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][0] == 0
    assert env.board[0][0] == 0
    assert board[0][1] == 1
    assert env.board[0][1] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][1] == 0
    assert env.board[0][1] == 0
    assert board[0][2] == 1
    assert env.board[0][2] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.RIGHT)

    assert board[0][2] == 1
    assert env.board[0][2] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert board[0][2] == 0
    assert env.board[0][2] == 0
    assert board[1][2] == 1
    assert env.board[1][2] == 1
    assert reward == env.reward_default
    assert done is False
    assert info['num_done_tasks'] == 0

    board, reward, done, info = env.step(GridTSP.DOWN)

    assert board[1][2] == 0
    assert env.board[1][2] == 0
    assert board[2][2] == 1
    assert env.board[2][2] == 1
    assert reward == 1
    assert done is True
    assert info['num_done_tasks'] == 1


def test2():
    env = GridTSP((3, 3), (0, 0), [(1, 0), (2, 2)])

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
    env = GridTSP((3, 3), (2, 1), [(1, 0), (2, 2)])

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

    board, reward, done, info = env.step(GridTSP.UP)

    assert reward == 1
    assert done is True
    assert info['num_done_tasks'] == 2
