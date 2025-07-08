"""
Reference:
http://www.slideshare.net/ishraqabd/publish-subscribe-model-overview-13368808
Author: https://github.com/HanWenfang
"""

from __future__ import annotations


class Provider:
    def __init__(self) -> None:
        self.msg_queue = []
        self.subscribers = {}

    def notify(self, msg: str) -> None:
        self.msg_queue.append(msg)

    def subscribe(self, msg: str, subscriber: Subscriber) -> None:
        self.subscribers.setdefault(msg, []).append(subscriber)

    def unsubscribe(self, msg: str, subscriber: Subscriber) -> None:
        self.subscribers[msg].remove(subscriber)

    def update(self) -> None:
        for msg in self.msg_queue:
            for sub in self.subscribers.get(msg, []):
                sub.run(msg)
        self.msg_queue = []


class Publisher:
    def __init__(self, msg_center: Provider) -> None:
        self.provider = msg_center

    def publish(self, msg: str) -> None:
        self.provider.notify(msg)


class Subscriber:
    def __init__(self, name: str, msg_center: Provider) -> None:
        self.name = name
        self.provider = msg_center

    def subscribe(self, msg: str) -> None:
        self.provider.subscribe(msg, self)

    def unsubscribe(self, msg: str) -> None:
        self.provider.unsubscribe(msg, self)

    def run(self, msg: str) -> None:
        print(f"{self.name} got {msg}")


def main():
    """
    >>> message_center = Provider()

    >>> fftv = Publisher(message_center)

    >>> jim = Subscriber("jim", message_center)
    >>> jim.subscribe("cartoon")
    >>> jack = Subscriber("jack", message_center)
    >>> jack.subscribe("music")
    >>> gee = Subscriber("gee", message_center)
    >>> gee.subscribe("movie")
    >>> vani = Subscriber("vani", message_center)
    >>> vani.subscribe("movie")
    >>> vani.unsubscribe("movie")

    # Note that no one subscribed to `ads`
    # and that vani changed their mind

    >>> fftv.publish("cartoon")
    >>> fftv.publish("music")
    >>> fftv.publish("ads")
    >>> fftv.publish("movie")
    >>> fftv.publish("cartoon")
    >>> fftv.publish("cartoon")
    >>> fftv.publish("movie")
    >>> fftv.publish("blank")

    >>> message_center.update()
    jim got cartoon
    jack got music
    gee got movie
    jim got cartoon
    jim got cartoon
    gee got movie
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
