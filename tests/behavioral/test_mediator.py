import pytest

from patterns.behavioral.mediator import User

def test_mediated_comments():
    molly = User('Molly')
    mediated_comment = molly.say("Hi Team! Meeting at 3 PM today.")
    assert mediated_comment == "[Molly says]: Hi Team! Meeting at 3 PM today."

    mark = User('Mark')
    mediated_comment = mark.say("Roger that!")
    assert mediated_comment == "[Mark says]: Roger that!"

    ethan = User('Ethan')
    mediated_comment = ethan.say("Alright.")
    assert mediated_comment == "[Ethan says]: Alright."
