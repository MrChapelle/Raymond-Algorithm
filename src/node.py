import pika

class Node():
	def __init__(self, number, holder, queue = [], using = False):
		self.number = number
		self.holder = holder
		self.queue  = queue
		self.using  = using 

#Getters -------------------------------------------------------
	def get_number(self):
		return self.number

	def get_holder(self):
		return self.holder

	def get_queue(self):
		return self.queue

	def is_using(self):
		return self.using
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
