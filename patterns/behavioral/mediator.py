#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://www.djangospin.com/design-patterns-python/mediator/

Objects in a system communicate through a Mediator instead of directly with each other.
This reduces the dependencies between communicating objects, thereby reducing coupling.

*TL;DR80
Encapsulates how a set of objects interact.
"""


class ChatRoom(object):
    """Mediator class"""

    def display_message(self, user, message):
        print("[{} says]: {}".format(user, message))


class User(object):
    """A class whose instances want to interact with each other"""

    def __init__(self, name):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message):
        self.chat_room.display_message(self, message)

    def __str__(self):
        return self.name


def main():
    molly = User('Molly')
    mark = User('Mark')
    ethan = User('Ethan')

    molly.say("Hi Team! Meeting at 3 PM today.")
    mark.say("Roger that!")
    ethan.say("Alright.")


if __name__ == '__main__':
    main()


OUTPUT = """
[Molly says]: Hi Team! Meeting at 3 PM today.
[Mark says]: Roger that!
[Ethan says]: Alright.
"""  # noqa
