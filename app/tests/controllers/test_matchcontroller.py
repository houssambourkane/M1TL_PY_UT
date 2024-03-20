from Controllers.MatchController import MatchController


class TestMatchController:
    def test_create_match_pairs(self):
        # Test avec une liste de joueurs paire
        players = ['Alice', 'Bob', 'Charlie', 'Diana']
        expected_pairs = [('Alice', 'Bob'), ('Charlie', 'Diana')]
        actual_pairs = MatchController().create_match_pairs(players)
        assert expected_pairs == actual_pairs

    def test_create_matches(self):
        # Test avec une liste de paires vide
        pairs = []
        expected_matches = []
        actual_matches = MatchController().create_matches(pairs)
        assert expected_matches == actual_matches

    def test_pair_players(self):
        # Test avec une liste de joueurs vide
        sorted_players = []
        played_matches = []
        expected_pairs = []
        actual_pairs = MatchController().pair_players(sorted_players, played_matches)
        assert expected_pairs == actual_pairs

    def test_has_played_together(self):
        # Test avec deux joueurs qui n'ont jamais joué ensemble
        player1 = {'first_name': 'Alice', 'last_name': 'Smith'}
        player2 = {'first_name': 'Bob', 'last_name': 'Jones'}
        played_matches = []
        assert not MatchController().has_played_together(player1, player2, played_matches)
