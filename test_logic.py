from logic import *


def test_is_tile_empty():
    grid = [
        [0, 2, 4, 8],
        [16, 32, 64, 128],
        [256, 512, 1024, 0],
        [2, 4, 8, 16]
    ]

    assert is_tile_empty(grid, 0, 0) is True
    assert is_tile_empty(grid, 0, 1) is False
    assert is_tile_empty(grid, 2, 3) is True


def test_is_grid_full_true():
    grid = [
        [2, 2, 4, 8],
        [16, 32, 64, 128],
        [256, 512, 1024, 2],
        [4, 8, 16, 32]
    ]

    assert is_grid_full(grid) is True


def test_is_grid_full_false():
    grid = [
        [2, 0, 4, 8],
        [16, 32, 64, 128],
        [256, 512, 1024, 2],
        [4, 8, 16, 32]
    ]

    assert is_grid_full(grid) is False


def test_gen_number():
    for _ in range(100):
        value = gen_number()
        assert value in [2, 4]


def test_gen_new_tile():
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    gen_new_tile(grid)

    non_zero = 0

    for row in grid:
        for value in row:
            if value != 0:
                non_zero += 1
                assert value in [2, 4]

    assert non_zero == 1


def test_move_left_simple_merge():
    grid = [
        [2, 2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    expected = [
        [4, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert move(grid, 'a') == expected


def test_move_left_multiple_merge():
    grid = [
        [2, 2, 4, 4],
        [8, 0, 8, 0],
        [2, 2, 2, 2],
        [4, 0, 0, 4]
    ]

    expected = [
        [4, 8, 0, 0],
        [16, 0, 0, 0],
        [4, 4, 0, 0],
        [8, 0, 0, 0]
    ]

    assert move(grid, 'a') == expected


def test_move_right():
    grid = [
        [2, 2, 0, 0],
        [4, 4, 4, 4],
        [2, 0, 2, 0],
        [8, 0, 0, 8]
    ]

    expected = [
        [0, 0, 0, 4],
        [0, 0, 8, 8],
        [0, 0, 0, 4],
        [0, 0, 0, 16]
    ]

    assert move(grid, 'd') == expected


def test_move_up():
    grid = [
        [2, 0, 2, 0],
        [2, 4, 2, 0],
        [0, 4, 0, 0],
        [0, 0, 0, 0]
    ]

    expected = [
        [4, 8, 4, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert move(grid, 'w') == expected


def test_move_down():
    grid = [
        [2, 0, 2, 0],
        [2, 4, 2, 0],
        [0, 4, 0, 0],
        [0, 0, 0, 0]
    ]

    expected = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [4, 8, 4, 0]
    ]

    assert move(grid, 's') == expected


def test_has_2048_true():
    grid = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 2],
        [4, 8, 16, 32]
    ]

    assert has_2048(grid) is True


def test_has_2048_false():
    grid = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2, 2],
        [4, 8, 16, 32]
    ]

    assert has_2048(grid) is False


def test_can_merge_horizontal():
    grid = [
        [2, 2, 4, 8],
        [16, 32, 64, 128],
        [256, 512, 1024, 2],
        [4, 8, 16, 32]
    ]

    assert can_merge(grid) is True


def test_can_merge_vertical():
    grid = [
        [2, 4, 8, 16],
        [2, 32, 64, 128],
        [256, 512, 1024, 2],
        [4, 8, 16, 32]
    ]

    assert can_merge(grid) is True


def test_can_merge_false():
    grid = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2, 4],
        [8, 16, 32, 64]
    ]

    assert can_merge(grid) is False