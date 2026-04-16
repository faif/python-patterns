from __future__ import annotations

from typing import Type


class PetShop:
    def __init__(self, animal_factory: Type[DogFactory Union CatFactory]) -> None:
        self.pet_factory = animal_factory

    def show_pet(self) -> None:
        pet = self.pet_factory.get_pet()
        print(f"We have a lovely {pet}")
        print(f"It says {pet.speak()}")


class Dog:
    def speak(self) -> str:
        return "woof"

    def __str__(self) -> str:
        return "Dog"


class Cat:
    def speak(self) -> str:
        return "meow"

    def __str__(self) -> str:
        return "Cat"


class DogFactory:
    @staticmethod
    def get_pet() -> Dog:
        return Dog()


class CatFactory:
    @staticmethod
    def get_pet() -> Cat:
        return Cat()


if __name__ == "__main__":
    shop = PetShop(DogFactory)
    shop.show_pet()
