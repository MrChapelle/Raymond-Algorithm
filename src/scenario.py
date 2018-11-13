import pika
import sys
from node import *

Node_0 = Node(0, 0, [], True)
Node_1 = Node(1, 0)
Node_2 = Node(2, 0)
Node_3 = Node(3, 2)
Node_4 = Node(4, 3)
Node_5 = Node(5, 3)

Node_5.ask_token_request()