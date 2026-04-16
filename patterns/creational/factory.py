from __future__ import annotations
from typing import Dict, Type


class GreekGetter:
    def __init__(self) -> None:
        self.trans: Dict[str, str] = {
            "dog": "σκύλος",
            "cat": "γάτα",
        }

    def get(self, msg: str) -> str:
        return self.trans.get(msg, msg)


class EnglishGetter:
    def get(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> GreekGetter | EnglishGetter:
    languages: Dict[str, Type[GreekGetter | EnglishGetter]] = {
        "English": EnglishGetter,
        "Greek": GreekGetter,
    }
    return languages[language]()


if __name__ == "__main__":
    for msg in ["dog", "cat", "bird"]:
        f = get_localizer("English")
        g = get_localizer("Greek")
        print(f"{f.get(msg)} == {g.get(msg)}")
