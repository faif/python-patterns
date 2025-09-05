"""
@author: Eugene Duboviy <eugene.dubovoy@gmail.com> | github.com/duboviy

In Blackboard pattern several specialised sub-systems (knowledge sources)
assemble their knowledge to build a possibly partial or approximate solution.
In this way, the sub-systems work together to solve the problem,
where the solution is the sum of its parts.

https://en.wikipedia.org/wiki/Blackboard_system
"""

from abc import ABC, abstractmethod
import random


class AbstractExpert(ABC):
    """Abstract class for experts in the blackboard system."""

    @abstractmethod
    def __init__(self, blackboard) -> None:
        self.blackboard = blackboard

    @property
    @abstractmethod
    def is_eager_to_contribute(self) -> int:
        raise NotImplementedError("Must provide implementation in subclass.")

    @abstractmethod
    def contribute(self) -> None:
        raise NotImplementedError("Must provide implementation in subclass.")


class Blackboard:
    """The blackboard system that holds the common state."""

    def __init__(self) -> None:
        self.experts: list = []
        self.common_state = {
            "problems": 0,
            "suggestions": 0,
            "contributions": [],
            "progress": 0,  # percentage, if 100 -> task is finished
        }

    def add_expert(self, expert: AbstractExpert) -> None:
        self.experts.append(expert)


class Controller:
    """The controller that manages the blackboard system."""

    def __init__(self, blackboard: Blackboard) -> None:
        self.blackboard = blackboard

    def run_loop(self):
        """
        This function is a loop that runs until the progress reaches 100.
        It checks if an expert is eager to contribute and then calls its contribute method.
        """
        while self.blackboard.common_state["progress"] < 100:
            for expert in self.blackboard.experts:
                if expert.is_eager_to_contribute:
                    expert.contribute()
        return self.blackboard.common_state["contributions"]


class Student(AbstractExpert):
    """Concrete class for a student expert."""

    def __init__(self, blackboard) -> None:
        super().__init__(blackboard)

    @property
    def is_eager_to_contribute(self) -> bool:
        return True

    def contribute(self) -> None:
        self.blackboard.common_state["problems"] += random.randint(1, 10)
        self.blackboard.common_state["suggestions"] += random.randint(1, 10)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(1, 2)


class Scientist(AbstractExpert):
    """Concrete class for a scientist expert."""

    def __init__(self, blackboard) -> None:
        super().__init__(blackboard)

    @property
    def is_eager_to_contribute(self) -> int:
        return random.randint(0, 1)

    def contribute(self) -> None:
        self.blackboard.common_state["problems"] += random.randint(10, 20)
        self.blackboard.common_state["suggestions"] += random.randint(10, 20)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(10, 30)


class Professor(AbstractExpert):
    def __init__(self, blackboard) -> None:
        super().__init__(blackboard)

    @property
    def is_eager_to_contribute(self) -> bool:
        return True if self.blackboard.common_state["problems"] > 100 else False

    def contribute(self) -> None:
        self.blackboard.common_state["problems"] += random.randint(1, 2)
        self.blackboard.common_state["suggestions"] += random.randint(10, 20)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(10, 100)


def main():
    """
    >>> blackboard = Blackboard()
    >>> blackboard.add_expert(Student(blackboard))
    >>> blackboard.add_expert(Scientist(blackboard))
    >>> blackboard.add_expert(Professor(blackboard))

    >>> c = Controller(blackboard)
    >>> contributions = c.run_loop()

    >>> from pprint import pprint
    >>> pprint(contributions)
     ['Student',
    'Scientist',
    'Student',
    'Scientist',
    'Student',
    'Scientist',
    'Professor']
    """


if __name__ == "__main__":
    random.seed(1234)  # for deterministic doctest outputs
    import doctest

    doctest.testmod()
