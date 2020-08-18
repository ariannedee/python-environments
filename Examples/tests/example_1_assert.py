from rock_paper_scissors_buggy import determine_winner, game_over, YOU, COMP


def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_determine_winner():
    test_cases = (
        ('r', 'r', None),
        ('r', 'p', COMP),
        ('r', 's', YOU),
        ('p', 'r', YOU),
        ('p', 'p', None),
        ('p', 's', COMP),
        ('s', 'r', COMP),
        ('s', 'p', YOU),
        ('s', 's', None),
    )

    for case in test_cases:
        you, comp, winner = case
        assert_equals(determine_winner(you, comp), winner)

    print('determine_winner tests passed')


def test_game_over():
    test_cases = (
        (3, [0, 0], None),
        (3, [1, 1], None),
        (3, [2, 1], YOU),
        (3, [1, 2], COMP),
        (5, [2, 2], None),
        (5, [3, 0], YOU),
        (5, [1, 3], COMP),
    )

    for case in test_cases:
        best_of, score, winner = case
        assert_equals(game_over(best_of, score), winner)

    print('game_over tests passed')


test_determine_winner()
test_game_over()
