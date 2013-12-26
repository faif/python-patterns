#!/usr/bin/env python

'''
Reference: http://www.slideshare.net/ishraqabd/publish-subscribe-model-overview-13368808
Author: https://github.com/HanWenfang
'''

class Provider:
	def __init__(self):
		self.msgQueue = []
		self.subscribers = {}

	def notify(self, msg):
		self.msgQueue.append(msg)

	def subscribe(self,msg, subscriber):
		if not msg in self.subscribers:
			self.subscribers[msg] = []
			self.subscribers[msg].append(subscriber) #unfair
		else:
			self.subscribers[msg].append(subscriber)
	
	def unSubscribe(self,msg, subscriber):
		self.subscribers[msg].remove(subscriber)

	def update(self):
		for msg in self.msgQueue:
			if msg in self.subscribers:
				for sub in self.subscribers[msg]:
					sub.run(msg)
		self.msgQueue = []

class Publisher:
	def __init__(self, msgCenter):
		self.provider = msgCenter
	
	def publish(self, msg):
		self.provider.notify(msg)


class Subscriber:
	def __init__(self,name,msgCenter):
		self.name = name
		self.provider = msgCenter

	def subscribe(self, msg):
		self.provider.subscribe(msg, self)

	def run(self, msg):
		print "%s got %s"%(self.name, msg)


def main():
	messageCenter = Provider()

	fftv = Publisher(messageCenter)

	jim = Subscriber("jim", messageCenter)
	jim.subscribe("cartoon")
	jack = Subscriber("jack", messageCenter)
	jack.subscribe("music")
	gee = Subscriber("gee", messageCenter)
	gee.subscribe("movie")

	fftv.publish("cartoon")
	fftv.publish("music")
	fftv.publish("ads")
	fftv.publish("movie")
	fftv.publish("cartoon")
	fftv.publish("cartoon")
	fftv.publish("movie")
	fftv.publish("blank")

	messageCenter.update()

if __name__ == "__main__":
	main()
