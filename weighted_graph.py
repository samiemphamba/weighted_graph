#!/usr/bin/env python

import heapq  # Needed for priority queue

"""
Purpose: 
	- Calculates the shortest distance between two districts(nodes)
Coder: 
	- Samson Kasambala Mphamba
Acknowledgement:
	- Dijkstra

Description:
	- It has method to add node(district name), to the dictionary
	- Also, you can add weight to the dictionary by associating two given nodes to the weight
	- It then creates a weighted graph instance
	- Lastly it calcultes shortest distance from A to B using breadth-first search (BFS)
"""

class WGraph:
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
   
	def dijkstra(self, start, end):
		"""
		Calculates the distance between two nodes in a weighted graph using Dijkstra's algorithm
		:param start: The starting node from which to calculate the distance
		:param end: The destination node to which the shortest distance is calculated
		:return: The shortest distance from the starting node to the destination node (float). distance as set
  
		"""
		distances = {node: float('inf') for node in self.graph}
		distances[start] = 0
		priority_queue = [(0, start)]

		while priority_queue:
			current_distance, current_node = heapq.heappop(priority_queue)

			if current_distance > distances[current_node]:
				continue

			for neighbor, weight in self.graph[current_node].items():
				distance = current_distance + weight

				if distance < distances[neighbor]:
					distances[neighbor] = distance
					heapq.heappush(priority_queue, (distance, neighbor))

		return distances[end]
	
