import json
import pytest
import os
from Models.Player import Player


# Assuming this code is in a test file
current_file_path = os.path.abspath(__file__)
data_dir = os.path.join(os.path.dirname(current_file_path), '../../data')
players_file_path = os.path.join(data_dir, 'players.json')


@pytest.fixture
def player_instance():
    return Player("John", "Doe", "1990-01-01", "123456")


def test_save_player(player_instance):
    player_instance.save_player()
    file_path = players_file_path
    with open(file_path, 'r') as file:
        players = json.load(file)
        assert players[0]['first_name'] == "John"
        assert players[0]['last_name'] == "Doe"


def test_get_players(player_instance, tmp_path):
    file_path = tmp_path / 'players.json'
    with open(file_path, 'w') as file:
        json.dump([player_instance.__dict__], file)
    loaded_players = player_instance.get_players()
    assert loaded_players[0]['first_name'] == "John"
