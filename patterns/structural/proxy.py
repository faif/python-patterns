from __future__ import annotations
from typing import Protocol


class Subject(Protocol):
    def request(self) -> None: ...


class RealSubject:
    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy:
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access...")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()
