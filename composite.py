#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A class which defines a composite object which can store
hieararchical dictionaries with names.

This class is same as a hiearchical dictionary, but it
provides methods to add/access/modify children by name,
like a Composite.

Created Anand B Pillai     <abpillai@gmail.com>

"""
__author__ = "Anand B Pillai"
__maintainer__ = "Anand B Pillai"
__version__ = "0.2"


def normalize(val):
    """ Normalize a string so that it can be used as an attribute
    to a Python object """

    if val.find('-') != -1:
        val = val.replace('-', '_')

    return val


def denormalize(val):
    """ De-normalize a string """

    if val.find('_') != -1:
        val = val.replace('_', '-')

    return val


class SpecialDict(dict):

    """ A dictionary type which allows direct attribute
    access to its keys """

    def __getattr__(self, name):

        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            # Check for denormalized name
            name = denormalize(name)
            if name in self:
                return self.get(name)
            else:
                raise AttributeError('no attribute named %s' % name)

    def __setattr__(self, name, value):

        if name in self.__dict__:
            self.__dict__[name] = value
        elif name in self:
            self[name] = value
        else:
            # Check for denormalized name
            name2 = denormalize(name)
            if name2 in self:
                self[name2] = value
            else:
                # New attribute
                self[name] = value


class CompositeDict(SpecialDict):

    """ A class which works like a hierarchical dictionary.
    This class is based on the Composite design-pattern """

    ID = 0

    def __init__(self, name=''):

        if name:
            self._name = name
        else:
            self._name = ''.join(('id#', str(self.__class__.ID)))
            self.__class__.ID += 1

        self._children = []
        # Link  back to father
        self._father = None
        self[self._name] = SpecialDict()

    def __getattr__(self, name):

        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            # Check for denormalized name
            name = denormalize(name)
            if name in self:
                return self.get(name)
            else:
                # Look in children list
                child = self.findChild(name)
                if child:
                    return child
                else:
                    attr = getattr(self[self._name], name)
                    if attr:
                        return attr

                    raise AttributeError('no attribute named %s' % name)

    def isRoot(self):
        """ Return whether I am a root component or not """

        # If I don't have a parent, I am root
        return not self._father

    def isLeaf(self):
        """ Return whether I am a leaf component or not """

        # I am a leaf if I have no children
        return not self._children

    def getName(self):
        """ Return the name of this ConfigInfo object """

        return self._name

    def getIndex(self, child):
        """ Return the index of the child ConfigInfo object 'child' """

        if child in self._children:
            return self._children.index(child)
        else:
            return -1

    def getDict(self):
        """ Return the contained dictionary """

        return self[self._name]

    def getProperty(self, child, key):
        """ Return the value for the property for child
        'child' with key 'key' """

        # First get the child's dictionary
        childDict = self.getInfoDict(child)
        if childDict:
            return childDict.get(key, None)

    def setProperty(self, child, key, value):
        """ Set the value for the property 'key' for
        the child 'child' to 'value' """

        # First get the child's dictionary
        childDict = self.getInfoDict(child)
        if childDict:
            childDict[key] = value

    def getChildren(self):
        """ Return the list of immediate children of this object """

        return self._children

    def getAllChildren(self):
        """ Return the list of all children of this object """

        l = []
        for child in self._children:
            l.append(child)
            l.extend(child.getAllChildren())

        return l

    def getChild(self, name):
        """ Return the immediate child object with the given name """

        for child in self._children:
            if child.getName() == name:
                return child

    def findChild(self, name):
        """ Return the child with the given name from the tree """

        # Note - this returns the first child of the given name
        # any other children with similar names down the tree
        # is not considered.

        for child in self.getAllChildren():
            if child.getName() == name:
                return child

    def findChildren(self, name):
        """ Return a list of children with the given name from the tree """

        # Note: this returns a list of all the children of a given
        # name, irrespective of the depth of look-up.

        children = []

        for child in self.getAllChildren():
            if child.getName() == name:
                children.append(child)

        return children

    def getPropertyDict(self):
        """ Return the property dictionary """

        d = self.getChild('__properties')
        if d:
            return d.getDict()
        else:
            return {}

    def getParent(self):
        """ Return the person who created me """

        return self._father

    def __setChildDict(self, child):
        """ Private method to set the dictionary of the child
        object 'child' in the internal dictionary """

        d = self[self._name]
        d[child.getName()] = child.getDict()

    def setParent(self, father):
        """ Set the parent object of myself """

        # This should be ideally called only once
        # by the father when creating the child :-)
        # though it is possible to change parenthood
        # when a new child is adopted in the place
        # of an existing one - in that case the existing
        # child is orphaned - see addChild and addChild2
        # methods !
        self._father = father

    def setName(self, name):
        """ Set the name of this ConfigInfo object to 'name' """

        self._name = name

    def setDict(self, d):
        """ Set the contained dictionary """

        self[self._name] = d.copy()

    def setAttribute(self, name, value):
        """ Set a name value pair in the contained dictionary """

        self[self._name][name] = value

    def getAttribute(self, name):
        """ Return value of an attribute from the contained dictionary """

        return self[self._name][name]

    def addChild(self, name, force=False):
        """ Add a new child 'child' with the name 'name'.
        If the optional flag 'force' is set to True, the
        child object is overwritten if it is already there.

        This function returns the child object, whether
        new or existing """

        if type(name) != str:
            raise ValueError('Argument should be a string!')

        child = self.getChild(name)
        if child:
            # print('Child %s present!' % name)
            # Replace it if force==True
            if force:
                index = self.getIndex(child)
                if index != -1:
                    child = self.__class__(name)
                    self._children[index] = child
                    child.setParent(self)

                    self.__setChildDict(child)
            return child
        else:
            child = self.__class__(name)
            child.setParent(self)

            self._children.append(child)
            self.__setChildDict(child)

            return child

    def addChild2(self, child):
        """ Add the child object 'child'. If it is already present,
        it is overwritten by default """

        currChild = self.getChild(child.getName())
        if currChild:
            index = self.getIndex(currChild)
            if index != -1:
                self._children[index] = child
                child.setParent(self)
                # Unset the existing child's parent
                currChild.setParent(None)
                del currChild

                self.__setChildDict(child)
        else:
            child.setParent(self)
            self._children.append(child)
            self.__setChildDict(child)


if __name__ == "__main__":
    window = CompositeDict('Window')
    frame = window.addChild('Frame')
    tfield = frame.addChild('Text Field')
    tfield.setAttribute('size', '20')

    btn = frame.addChild('Button1')
    btn.setAttribute('label', 'Submit')

    btn = frame.addChild('Button2')
    btn.setAttribute('label', 'Browse')

    # print(window)
    # print(window.Frame)
    # print(window.Frame.Button1)
    # print(window.Frame.Button2)
    print(window.Frame.Button1.label)
    print(window.Frame.Button2.label)

### OUTPUT ###
# Submit
# Browse
