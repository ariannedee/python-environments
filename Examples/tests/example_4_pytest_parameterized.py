"""
import pytest
In terminal, run $ pytest
"""
import pytest

from .rock_paper_scissors_buggy import determine_winner, game_over, YOU, COMP


@pytest.mark.parametrize("you, comp, expected_winner", [
    ('r', 'r', None),
    ('r', 'p', COMP),
    ('r', 's', YOU),
    ('p', 'r', YOU),
    ('p', 'p', None),
    ('p', 's', COMP),
    ('s', 'r', COMP),
    ('s', 'p', YOU),
    ('s', 's', None),
])
def test_determine_winner(you, comp, expected_winner):
    assert determine_winner(you, comp) == expected_winner


@pytest.mark.parametrize("best_of, score, expected_winner", [
    (3, [0, 0], None),
    (3, [1, 1], None),
    (3, [2, 1], YOU),
    (3, [1, 2], COMP),
    (5, [2, 2], None),
    (5, [3, 0], YOU),
    (5, [1, 3], COMP)
])
def test_game_over(best_of, score, expected_winner):
    assert game_over(best_of, score) == expected_winner
