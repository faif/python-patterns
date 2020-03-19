from unittest.mock import patch, Mock

import pytest

from patterns.behavioral.observer import Data, DecimalViewer, HexViewer


@pytest.fixture
def observable():
    return Data('some data')

def test_attach_detach(observable):
    decimal_viewer = DecimalViewer()
    assert len(observable._observers) == 0

    observable.attach(decimal_viewer)
    assert decimal_viewer in observable._observers

    observable.detach(decimal_viewer)
    assert decimal_viewer not in observable._observers

def test_one_data_change_notifies_each_observer_once(observable):
    observable.attach(DecimalViewer())
    observable.attach(HexViewer())

    with patch('patterns.behavioral.observer.DecimalViewer.update', new_callable=Mock()) as mocked_update:
        assert mocked_update.call_count == 0
        observable.data = 10
        assert mocked_update.call_count == 1
