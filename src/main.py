import pika
import sys

# To do it correctly i have to change the node 5 parameters 
number = 5 # Node 5 will ask for the token 
holder = 3 # Node 5 will ask to his holder 3
body = "REQUEST TOKEN from node " + str(number)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_publish(exchange='',
                      routing_key=str(holder),
                      body=body)
print(" [*] Sent " + body + " to queue " + str(holder))
connection.close()

