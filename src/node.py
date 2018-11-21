import pika
import time

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
		if self.has_token() :
			self.using = True
		else :
			print(" [*] You are not the holder, you can't be in critical section")

	def stop_using(self):
		if self.using and self.has_token():
			self.using = False
		else :
			print(" [*] You are not in critical section because you are not the root or not using the token")	

	def ask_token_request(self):
		"""
		Function used by a node to ask the token
		It is used by the first node (5)
		"""
		if self.has_token():
			print(" [*] You already have the token")
		else :
			holder = self.get_holder()
			number = self.get_number()
			body = "REQUEST TOKEN from node " + str(number)

			connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
			channel    = connection.channel()
			channel.basic_publish(exchange='',
                      			routing_key=str(holder),
                      			body=body)
			print(" [*] Sent " + body + " to queue " + str(holder))
			connection.close()
			
			self.add_elem_queue(number)
			self.asked = True

	def transfer_token_request(self, requestor):
		"""
		Function used by a node to transfer the ask token request to 
		his parent (ex: 3 -> 2)
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
			print(" [*] Sent " + body + " to queue " + str(holder))
			connection.close()
			
			self.add_elem_queue(requestor)
			self.asked = True
			print(" [*] Message send")
			print(" [*] My queue :" + str(self.queue))
			print(" [*] Have I asked ? : " + str(self.asked))
			print(" [*] My holder : " + str(self.holder))
			print(" [*] Am I using ? : " + str(self.using))

	def send_token(self, requestor):
		if self.number == requestor :
			print(" [*] I made the request")
			self.holder = self.number
			self.asked = False
			self.start_using()
		else:
			body = "SEND TOKEN"

			connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
			channel    = connection.channel()
			channel.basic_publish(exchange='',
	                      routing_key=str(requestor),
	                      body=body)
			print(" [*] Sent " + body + " to queue " + str(requestor))
			self.holder = requestor
			self.asked = False
			connection.close()
		print(" [*] Message send")
		print(" [*] My queue :" + str(self.queue))
		print(" [*] Have I asked ? : " + str(self.asked))
		print(" [*] My holder : " + str(self.holder))
		print(" [*] Am I using ? : " + str(self.using))

	def transfer_token(self):
		#print("to implement")
		try:
			elem = self.queue.pop(0)
			self.send_token(elem)
		except:
			print("Cannot pop element, queue empty")

	# Init ------------------------------------------------------------------------------			

	def init_queue(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		channel    = connection.channel()
		queue = str(self.get_number())
		channel.queue_declare(queue = queue, durable = True)
		print(" [*] Queue " + str(self.get_number()) + " started")

		def callback(ch, method, properties, body):
			if body.count("REQUEST INIT".encode()):
				print(" [*] I initialize a request ")
				self.add_elem_queue(self.number)
				self.asked = True
			elif body.count("REQUEST TOKEN".encode()):
				requestor = int(body.replace("REQUEST TOKEN from node ".encode(),"".encode()))
				print(" [*] Received TOKEN REQUEST from node " + str(requestor))

				if self.has_token():
					print(" [*] I am the holder")
					if not self.is_using():
						print(" [*] I am not using the token")
						self.send_token(requestor)
					else :
						t = 0
						while self.is_using() and (t <= 5):  #we simulate a using time at 10s (arbitrary)
							print(" [*] I am using the token since " + str(t) + " seconds")
							t += 1
							time.sleep(1)
						self.stop_using()
						self.send_token(requestor)

				else :
					print(" [*] I don't have the token, I transfer the REQUEST to my holder")
					self.transfer_token_request(requestor)
			elif body.count("SEND TOKEN".encode()):
				self.transfer_token()
			else :
				print(" [*] Received %r" % body)

		channel.basic_consume(callback, queue=str(self.get_number()), no_ack=True)
		print(' [*] Waiting for messages. To exit press CTRL+C')
		channel.start_consuming()