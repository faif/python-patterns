from patterns.structural.facade import ComputerFacade


def test_computer_facade_start(capsys):
    cf = ComputerFacade()
    cf.start()
    out = capsys.readouterr().out
    assert "Freezing processor." in out
    assert "Loading from 0x00 data:" in out
    assert "Jumping to: 0x00" in out
    assert "Executing." in out
