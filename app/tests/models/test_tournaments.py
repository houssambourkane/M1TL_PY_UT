import json
import pytest
from Models.Tournament import Tournament
import os


# Assuming this code is in a test file
current_file_path = os.path.abspath(__file__)
data_dir = os.path.join(os.path.dirname(current_file_path), '../../data')
players_file_path = os.path.join(data_dir, 'tournaments.json')


# Define fixtures if needed
@pytest.fixture
def sample_tournament_data():
    return {
        "name": "Exemple Tournament",
        "location": "Exemple Location",
        "start_date": "2024-03-01",
        "end_date": "2024-03-05",
        "rounds": 4,
        "current_round": 1,
        "round_list": [],
        "player_list": [],
        "description": "Exemple Description"
    }


# Write test functions
def test_save__and_get_tournament(sample_tournament_data):
    # Create an instance of the Tournament class
    tournament = Tournament(**sample_tournament_data)
    # Call the save_tournament method
    tournament.save_tournament()
    file_path = players_file_path
    # Check if the data is correctly saved in the file
    with open(file_path, 'r') as file:
        data = json.load(file)
        assert data[0]["name"] == sample_tournament_data["name"]
    tournaments = tournament.get_tournaments()
    # Check if the returned data matches the sample data
    assert tournaments[0]["name"] == sample_tournament_data["name"]
