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
	
	def insert_edge(self, n1, n2, w):
		# check if n1 and n2 are in graph.
		# This will prevent us from adding null nodes
		if n1 in self.graph and n2 in self.graph:
			# From the graph, it looks undirected.
			# So it is a must to associate the nodes in two possible directions
			# From A to B = 10 or B to A = 10
			self.graph[n1][n2] = w
			self.graph[n2][n1] = w
	