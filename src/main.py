import pika
import sys
import time

# To do it correctly i have to change the node 5 parameters 
number = 5 # Node 5 will ask for the token 
holder = 3 # Node 5 will ask to his holder 3
begin = "REQUEST INIT from node " + str(number) 
body = "REQUEST TOKEN from node " + str(number)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_publish(exchange='',
                      routing_key=str(number),
                      body=begin)
print(" [*] Sent " + begin + " to queue " + str(number))
channel.basic_publish(exchange='',
                      routing_key=str(holder),
                      body=body)
print(" [*] Sent " + body + " to queue " + str(holder))

# time.sleep(10)
# print("Other request simulation")

# number = 1
# holder = 0
# begin = "REQUEST INIT from node " + str(number)
# body = "REQUEST TOKEN from node " + str(number)
# channel.basic_publish(exchange='',
#                       routing_key=str(number),
#                       body=begin)
# print(" [*] Sent " + begin + " to queue " + str(number))
# channel.basic_publish(exchange='',
#                       routing_key=str(holder),
#                       body=body)
# print(" [*] Sent " + body + " to queue " + str(holder))
connection.close()

