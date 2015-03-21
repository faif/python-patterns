#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://en.wikipedia.org/wiki/Abstract_factory_pattern

"""Implementation of the abstract factory pattern"""

from abc import ABCMeta, abstractmethod

# Factories


class AbstractFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_text(self, content):
        pass

    @abstractmethod
    def create_picture(self, path, name):
        pass


class HtmlFactory(AbstractFactory):
    def create_picture(self, path, name):
        return HtmlPicture(path, name)

    def create_text(self, content):
        return HtmlText(content)


class JsonFactory(AbstractFactory):
    def create_picture(self, path, name):
        return JsonPicture(path, name)

    def create_text(self, content):
        return JsonText(content)


# Entities

class MediaInterface():
    def render(self):
        raise NotImplementedError


class AbstractPicture():
    __metaclass__ = ABCMeta

    def __init__(self, path, name):
        self._path = str(path)
        self._name = str(name)


class AbstractText():
    __metaclass__ = ABCMeta

    def __init__(self, content):
        self._content = str(content)


class HtmlPicture(AbstractPicture, MediaInterface):
    def render(self):
        return '<img src="{path}" title="{name}" />'.format(path=self._path, name=self._name)


class HtmlText(AbstractText, MediaInterface):
    def render(self):
        return '<div>{content}</div>'.format(content=self._content)


class JsonPicture(AbstractPicture, MediaInterface):
    def render(self):
        import json

        return json.dumps({'type': 'picture', 'name': self._name, 'path': self._path})


class JsonText(AbstractText, MediaInterface):
    def render(self):
        import json

        return json.dumps({'type': 'text', 'content': self._content})


# Client factory call

def get_factory():
    import random

    """
    Let's be dynamic!
    :rtype: AbstractFactory
    """
    return random.choice([HtmlFactory, JsonFactory])()

# Display picture and text in specific environment
if __name__ == "__main__":
    for i in range(3):
        elements_factory = get_factory()
        picture = elements_factory.create_picture('path/to/image.jpg', 'sample image')
        text = elements_factory.create_text('This is our test text')

        if isinstance(elements_factory, HtmlFactory):
            print "Rendering html for a page response:"
        else:
            print "Rendering json for an API response:"

        print picture.render()
        print text.render()
        print("=" * 20)

### OUTPUT ###
# Rendering html for a page response:
# <img src="path/to/image.jpg" title="sample image" />
# <div>This is our test text</div>
# ====================
# Rendering html for a page response:
# <img src="path/to/image.jpg" title="sample image" />
# <div>This is our test text</div>
# ====================
# Rendering html for a page response:
# <img src="path/to/image.jpg" title="sample image" />
# <div>This is our test text</div>
# ====================
