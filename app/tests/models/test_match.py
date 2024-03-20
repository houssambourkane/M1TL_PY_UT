from Models.Match import Match


def test_serialize_match():
    player1 = {'first_name': 'John', 'last_name': 'Doe'}
    player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
    match = Match(player1, player2)
    serialized_match = match.serialize()
    assert serialized_match == {'player1': player1, 'player2': player2, 'winner': None}


def test_str_representation():
    player1 = {'first_name': 'John', 'last_name': 'Doe'}
    player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
    match = Match(player1, player2)
    expected_str = "John Doe VS Jane Doe"
    assert str(match) == expected_str
