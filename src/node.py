import pika

class Node():
	def __init__(self, number, parent, token):
		self.number = number
		self.parent = parent
		self.token  = token

#Getters -------------------------------------------------------
	def get_number(self):
		return self.number

	def has_token(self):
		return self.token

	def get_queue_to_ask(self):
		return self.parent

#Methods -------------------------------------------------------
	def init_queue(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		channel    = connection.channel()
		channel.queue_declare(queue = str(self.get_number))

	def ask_token(self):
		if has_token(self):
			print("You already have the token")
		else :
			queue_to_ask = self.get_queue_to_ask()
			if queue_to_ask == None :
				print("You are the root")
			else :
				print("to continue")

	def get_request(self):
		print("to continue")
