#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: https://github.com/fousteris-dim
Reference: http://en.wikipedia.org/wiki/Null_Object_pattern
"""

class Item:
	"""Represents an abstract item"""
	def __init__(self):
		self._value = None
		
	def setValue(self, value):
		self._value = value
	
class RealItem(Item):
	"""Represent a valid real item"""
	def __init__(self, value):
		self._value = value

	def printValue(self):
		print 'The value is: ' + str(self._value)
		
class NullItem(Item):
	"""Represents a null item. This is treated like real items except having no value"""
	def printValue(self):
		print '[Null object. No value]'
		
class ItemStore:
	"""Stores key/value pairs of items"""
	nullItem = NullItem()
	
	def __init__(self):
		self._items = {};
	
	def getItem(self, name):
		return self._items.setdefault(name, ItemStore.nullItem)
	
	def setItem(self, name, value):
		item = self._items.setdefault(name, None)
		if item != None:
			item.setValue(value)
		else:
			self._items[name] = RealItem(value)
		
itemstore = ItemStore()
itemstore.setItem('item2', 'test item2')

itemstore.getItem('item2').printValue()
itemstore.getItem('item3').printValue()

### OUTPUT ###
# The value is: test item2
# [Null object. No value]