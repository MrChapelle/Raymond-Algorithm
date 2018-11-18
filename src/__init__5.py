import pika
import sys
from node import *

def init_system():
	"""
	Function which create the initial queue of a node
	"""
	Node_5.init_queue()

if __name__ == '__main__':

	# Graph Creation
	Node_5 = Node(5, 3)

	#Queue Initialization
	init_system()
	#Pour qu un noeud souhaite entrer en fonction critique...il faudrait qu un element exterieur, c est a dire nous les dvpeurs, envoient un message specifique
	#que le noeud interpretera comme, je veux entrer en section critique