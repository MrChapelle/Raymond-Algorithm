import pika

class Node():
	def __init__(self, number, holder, queue = [], using = False, asked = False):
		self.number = number
		self.holder = holder
		self.queue  = queue
		self.using  = using 
		self.asked  = asked

#Getters and basic functions-------------------------------------
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

	def add_elem_queue(self, elem):
		self.queue.append(elem)

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

	def send_message(connect, queue, body):
		connection = pika.BlockingConnection(pika.ConnectionParameters(connect))
		channel    = connection.channel()
		channel.basic_publish(exchange='',
                      		routing_key=queue,
                      		body=body)
		print(" [x] Sent " + body + "to queue " + queue)
		connection.close()

	def ask_token_request(self):
		"""
		Function used by a node to ask the token
		It is used by the first node (5)
		"""
		if self.has_token():
			print("You already have the token")
		else :
			holder = self.get_holder()
			number = self.get_number()
			body = "REQUEST TOKEN from node " + str(number)
			connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
			channel    = connection.channel()
			channel.basic_publish(exchange='',
                      			routing_key=str(holder),
                      			body=body)
			print(" [x] Sent " + body + " to queue " + str(holder))
			connection.close()
			self.add_elem_queue(number)
			self.asked = True

	def transfer_token_request(self, asker):
		"""
		Function used by a node to transfer the ask token request to 
		his parent (ex: 3 -> 2)
		"""
		holder = self.get_holder()
		number = self.get_number()
		body = "REQUEST TOKEN from node " + str(number)
		send_message('localhost', str(holder), body)
		add_elem_queue(asker)
		self.asked = True			

	def send_token(self):
		if not has_token(self) or is_using(self):
			print("You can't send the token, you don't hold it or you're still using it")
		else:
			print("to implement")

	# Init ------------------------------------------------------------------------------			

	def init_queue(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		channel    = connection.channel()
		channel.queue_declare(queue = str(self.get_number))
		def callback(ch, method, properties, body):
			#Faire ici dans le callback les différents cas de figures selon le contenu du message et l'état du noeud
			print(" [x] Received %r" % body)

		channel.basic_consume(callback, queue=str(self.get_number), no_ack=True)
		print(' [*] Waiting for messages. To exit press CTRL+C')
		channel.start_consuming()