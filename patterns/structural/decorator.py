"""
*What is this pattern about?
The Decorator pattern is used to dynamically add a new feature to an
object without changing its implementation. It differs from
inheritance because the new feature is added only to that particular
object, not to the entire subclass.

*What does this example do?
This example shows a way to add formatting options (boldface and
italic) to a text by appending the corresponding tags (<b> and
<i>). Also, we can see that decorators can be applied one after the other,
since the original text is passed to the bold wrapper, which in turn
is passed to the italic wrapper.

*Where is the pattern used practically?
The Grok framework uses decorators to add functionalities to methods,
like permissions or subscription to an event:
http://grok.zope.org/doc/current/reference/decorators.html

*References:
https://sourcemaking.com/design_patterns/decorator

*TL;DR
Adds behaviour to object without affecting its class.
"""


class TextTag:
    """Represents a base text tag"""

    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"


def main():
    """
    >>> simple_hello = TextTag("hello, world!")
    >>> special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    >>> print("before:", simple_hello.render())
    before: hello, world!

    >>> print("after:", special_hello.render())
    after: <i><b>hello, world!</b></i>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
