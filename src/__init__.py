import pika
import sys
from node import *

def init_system():
	"""
	Function which create the initial state of the graph
	"""

	Graph = [Node_0, Node_1, Node_2, Node_3, Node_4, Node_5]

	for node in Graph :
		node.init_queue()

if __name__ == '__main__':

	# Graph Creation
	Node_0 = Node(0, 0, [], True)
	Node_1 = Node(1, 0)
	Node_2 = Node(2, 0)
	Node_3 = Node(3, 2)
	Node_4 = Node(4, 3)
	Node_5 = Node(5, 3)

	#Queue Initialization
	init_system()
	#Pour qu'un noeud souhaite entrer en fonction critique...il faudrait qu'un élément extérieur, c'est à dire nous les dvpeurs, envoient un message spécifique
	#que le noeud interpretera comme, "je veux entrer en section critique"