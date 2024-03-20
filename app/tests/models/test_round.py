import pytest
from Models.Rounds import Round


@pytest.fixture
def sample_round():
    return Round(round_number=1, round_name="First Round", matches=[])


def test_serialize(sample_round):
    serialized_data = sample_round.serialize()
    assert serialized_data['round_number'] == 1
    assert serialized_data['round_name'] == "First Round"
    assert serialized_data['matches'] == []
