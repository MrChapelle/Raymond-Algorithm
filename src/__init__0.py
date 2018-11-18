import pika
import sys
from node import *

def init_system():
	"""
	Function which create the initial queue of a node
	"""
	Node_0.init_queue()

if __name__ == '__main__':

	# Graph Creation
	Node_0 = Node(0, 0, [], False)

	#Queue Initialization
	init_system()
	#Pour qu un noeud souhaite entrer en fonction critique...il faudrait qu un element exterieur, c est a dire nous les dvpeurs, envoient un message specifique
	#que le noeud interpretera comme, je veux entrer en section critique