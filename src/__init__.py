import pika
import sys
from node import *

def init_system():
	"""
	Function which create the initial state of the graph
	"""
	Node_0 = Node(0, None, True)
	Node_1 = Node(1, 0,    False)
	Node_2 = Node(2, 0,    False)
	Node_3 = Node(3, 2,    False)
	Node_4 = Node(4, 3,    False)
	Node_5 = Node(5, 3,    False)

	Graph = [Node_0, Node_1, Node_2, Node_3, Node_4, Node_5]

	for node in Graph :
		node.init_queue()

if __name__ == '__main__':
	init_system()