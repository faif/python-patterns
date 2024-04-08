import pytest

from patterns.behavioral.memento import NumObj, Transaction

def test_object_creation():
    num_obj = NumObj(-1)
    assert repr(num_obj) == '<NumObj: -1>', "Object representation not as expected"

def test_rollback_on_transaction():
    num_obj = NumObj(-1)
    a_transaction = Transaction(True, num_obj)
    for _i in range(3):
        num_obj.increment()
    a_transaction.commit()
    assert num_obj.value == 2

    for _i in range(3):
        num_obj.increment()
    try:
        num_obj.value += 'x'  # will fail
    except TypeError:
        a_transaction.rollback()
    assert num_obj.value == 2, "Transaction did not rollback as expected"

def test_rollback_with_transactional_annotation():
    num_obj = NumObj(2)
    with pytest.raises(TypeError):
        num_obj.do_stuff()
    assert num_obj.value == 2
