import pika
import sys
from node import *

def init_system():
	"""
	Function which create the initial queue of a node
	"""
	Node_3.init_queue()

if __name__ == '__main__':

	# Graph Creation
	Node_3 = Node(3, 2)

	#Queue Initialization
	init_system()
	#Pour qu'un noeud souhaite entrer en fonction critique...il faudrait qu'un élément extérieur, c'est à dire nous les dvpeurs, envoient un message spécifique
	#que le noeud interpretera comme, "je veux entrer en section critique"