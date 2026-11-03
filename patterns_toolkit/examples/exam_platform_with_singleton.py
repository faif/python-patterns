"""
Example: Singleton Pattern Applied to an Online Exam Platform
==============================================================
This example shows how the Singleton pattern can be used for
a centralized exam configuration that is shared across all
parts of the platform.

This directly relates to an Online Exam Platform project,
demonstrating how design patterns integrate into real-world applications.
"""

from __future__ import annotations
from typing import Any, Dict


class Singleton:
    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class ExamConfig(Singleton):
    """
    Centralized exam configuration.
    All modules (timer, grading, question loader) share the same config.
    """

    _initialized: bool = False

    def __init__(self) -> None:
        if self._initialized:
            return
        self._settings: Dict[str, Any] = {
            "time_limit_minutes": 60,
            "passing_score": 50,
            "shuffle_questions": True,
            "show_results_immediately": False,
            "max_attempts": 3,
        }
        self._initialized = True

    def get(self, key: str) -> Any:
        return self._settings.get(key)

    def set(self, key: str, value: Any) -> None:
        self._settings[key] = value


class ExamTimer:
    """Timer module that reads time limit from the shared config."""

    def get_time_limit(self) -> str:
        config = ExamConfig()
        minutes = config.get("time_limit_minutes")
        return f"Exam time limit: {minutes} minutes"


class ExamGrader:
    """Grading module that reads passing score from the shared config."""

    def check_result(self, score: int) -> str:
        config = ExamConfig()
        passing = config.get("passing_score")
        if score >= passing:
            return f"Score {score}/{100}: PASSED (minimum: {passing})"
        return f"Score {score}/{100}: FAILED (minimum: {passing})"


class QuestionLoader:
    """Question module that checks shuffle setting from the shared config."""

    def load_questions(self) -> str:
        config = ExamConfig()
        shuffle = config.get("shuffle_questions")
        if shuffle:
            return "Loading questions in random order..."
        return "Loading questions in original order..."


def main():
    """
    >>> timer = ExamTimer()
    >>> grader = ExamGrader()
    >>> loader = QuestionLoader()

    # All modules read from the SAME config instance
    >>> timer.get_time_limit()
    'Exam time limit: 60 minutes'

    >>> grader.check_result(75)
    'Score 75/100: PASSED (minimum: 50)'

    >>> grader.check_result(30)
    'Score 30/100: FAILED (minimum: 50)'

    >>> loader.load_questions()
    'Loading questions in random order...'

    # Admin changes the config - all modules see the change immediately
    >>> admin_config = ExamConfig()
    >>> admin_config.set("time_limit_minutes", 90)
    >>> admin_config.set("passing_score", 60)
    >>> admin_config.set("shuffle_questions", False)

    >>> timer.get_time_limit()
    'Exam time limit: 90 minutes'

    >>> grader.check_result(55)
    'Score 55/100: FAILED (minimum: 60)'

    >>> loader.load_questions()
    'Loading questions in original order...'
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()