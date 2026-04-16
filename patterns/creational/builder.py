from __future__ import annotations
from typing import Any


class Director:
    def __init__(self) -> None:
        self.builder: Any = None

    def construct_building(self) -> None:
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self) -> Any:
        return self.builder.building


class Builder:
    def __init__(self) -> None:
        self.building: Any = None

    def new_building(self) -> None:
        self.building = Building()


class BuilderHouse(Builder):
    def build_floor(self) -> None:
        self.building.floor = "One"

    def build_size(self) -> None:
        self.building.size = "Big"


class Building:
    def __init__(self) -> None:
        self.floor: str | None = None
        self.size: str | None = None

    def __repr__(self) -> str:
        return f"Floor: {self.floor} | Size: {self.size}"


if __name__ == "__main__":
    director = Director()
    director.builder = BuilderHouse()
    director.construct_building()
    print(director.get_building())
