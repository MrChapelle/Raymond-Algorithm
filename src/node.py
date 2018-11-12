import pika

class Node():
	def __init__(self, number, holder, queue = [], using = False, asked = False):
		self.number = number
		self.holder = holder
		self.queue  = queue
		self.using  = using 
		self.asked  = asked

#Getters -------------------------------------------------------
	def get_number(self):
		return self.number

	def get_holder(self):
		return self.holder

	def get_queue(self):
		return self.queue

	def is_using(self):
		return self.using

	def has_token(self):
		return self.number == self.holder


#Methods -------------------------------------------------------
	
	def start_using(self):
		if has_token(self) :
			self.using = True
		else :
			print("You are not the holder, you can't be in critical section")

	def stop_using(self):
		if self.using and has_token(self):
			self.using = False
		else :
			print("You are not in critical section because you are not the root or not using the token")	

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
