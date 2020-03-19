import pytest

from patterns.behavioral.state import Radio


@pytest.fixture
def radio():
    return Radio()

def test_initial_state(radio):
    assert radio.state.name == 'AM'

def test_initial_am_station(radio):
    initial_pos = radio.state.pos
    assert radio.state.stations[initial_pos] == '1250'

def test_toggle_amfm(radio):
    assert radio.state.name == 'AM'

    radio.toggle_amfm()
    assert radio.state.name == 'FM'

    radio.toggle_amfm()
    assert radio.state.name == 'AM'
