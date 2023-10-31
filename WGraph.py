#!/usr/bin/env python

"""

wGraph initializes a dictionary. 
It has method to add node(district name), to the dictionary
Also, you can add weight to the dictionary by associating two given nodes to the weight
It then creates a weighted graph instance
Lastly it calcultes shortest distance from A to B

"""

class wGraph:
	def __init__(self):
		self.graph = {} #   dictionary
	def insert_node(self, n):
		# add new node to the dictinary if does not exits
		# This assign district name a key to this node
		if n not in self.graph:
			self.graph[n] = {}